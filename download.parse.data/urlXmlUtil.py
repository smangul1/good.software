
import xml.etree.ElementTree
import re
import httplib
from urlparse import urlparse

def checkUrl(url):
	try:
		p = urlparse(url)
		conn = httplib.HTTPConnection(p.netloc,timeout=10)
		conn.request('HEAD', p.path)
		resp = conn.getresponse()
		return str(resp.status) # @resp.status is the 404 or 302 or whatever http code name
	except:
		return "-1" # connection timeout. but why does it timeout ??

def stringBetween (text,tag1,tag2) :
	end1 = re.search(tag1, text).span()[1]
	end2 = re.search(tag2, text).span()[0]
	return text[end1:end2]

def getPaperPmid ( paperName ):
	tree = xml.etree.ElementTree.parse(paperName)
	##
	paperPmid = ''
	for node in tree.iter():
		if node.tag == "article-id" :
			if (node.attrib['pub-id-type'] == "pmid"):
				paperPmid = node.text
				break # only need pmid
	if len(paperPmid)==0:
		paperPmid='NA'
	return paperPmid

def getPaperYear( paperName ):
	tree = xml.etree.ElementTree.parse(paperName)
	##
	paperYear = ''
	for node in tree.iter():
		if node.tag == "year" :
			paperYear = node.text
			break # only need 1st year, so quit right after.
	if len(paperYear)==0:
		paperYear='NA'
	return paperYear

def isSoftware (text, link): # @text should be full text (not @abstract)
	linkSpan = re.search(re.escape(link), text).span() # position of link
	left = linkSpan[0]-75 ## character including spacing. so ... about 5-10 words
	if left < 0:
		left = 0

	right = linkSpan[1]+75

	if right > len(text):
		right = len(text)

	leftWindow = text [ left : linkSpan[0] ] ## look left
	rightWindow = text [ linkSpan[1] : right ] ## look right

	#
	TARGET = [ "here", "pipeline", "code", "software", "available", "publicly", "tool", "method", "algorithm", "download", "application", "apply", "package", "library" ]
	for targetTagWord in TARGET:
		if targetTagWord in leftWindow:
			return targetTagWord
		if targetTagWord in rightWindow:
			return targetTagWord
	return "null"

def isNodeTag (node,nodeTag): ## Breadth-first search approach.
  queue = [node]
  if node.tag == nodeTag:
    return [node]
  if len(node.getchildren())==0:
		return [] ## this purposely triggers an error
  queue.remove(node)
  queue = queue + node.getchildren()
  node2return = [] ## @node2return nodes matching the pattern. ie. <ext-link>
  while len(queue)>0: ## not empty
    node = queue[0] ## node to be removed
    queue.remove(node)
    if node.tag == nodeTag:
      node2return.append(node)
    if len(node.getchildren())>0: ## add more nodes to "probe"
      queue = queue + node.getchildren()
  return node2return

def getLinkInNode (linkNode):
	if linkNode.text == None:
		return linkNode.items()[0][1]
	else:
		return linkNode.text

def getHttpStatus (paperName,where):
	pmid = getPaperPmid ( paperName )
	pYear = getPaperYear (paperName)
	linkStatus = getLinkInBody (paperName,where)
	return str(pmid) + " " + str(pYear) + " " + linkStatus

def getLinkInBody ( paperName, where="abstract" )	: # @where is abstract or body
	tree = xml.etree.ElementTree.parse(paperName)
	root = tree.getroot()
	bodyNode = isNodeTag(root,where)
	if len(bodyNode) == 0:
		return where+"NotFound" ## no tag for this paper
	##
	httpLinks = isNodeTag(bodyNode[0],'ext-link') ## get all links in <body>
	if len(httpLinks)==0:
		return 'NoLink' ## nothing found for this paper
	linkStatus = ""
	text = open (paperName ,"r").read() # @text is the entire paper
	text = stringBetween ( text,"<"+where+">", "</"+where+">" )
	for linkNode in httpLinks:
		link = getLinkInNode(linkNode)
		if ("Supplementary" in link) | ("supplementary" in link): ## outlink to supp. but not real internet link.
			continue
		try:
			targetTagWord = isSoftware(text, link)
		except:
			continue
		# targetTagWord = "null"
		link = re.sub(" ","",link)
		# link = link.strip()
		status = checkUrl(link)
		linkStatus = linkStatus + targetTagWord + " " + link + " " + status + " " ## triplet "tag + link + http_code"
	return linkStatus.encode('utf-8')
