#Till now we saved data in text file or database but sometime we dont need big database
#but just small structure for that we use XML

#XML stands for Extinsible Markup Language :: It is platform independent

#SAX:: Simple API for XML
#suited for large XML files or in situation with limited RAM
#In this we read from hard drive and only load little parts that we need 
import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(name)

handler = GroupHandler()

parser = xml.sax.make_parser()

parser.setContentHandler(handler)
parser.parse("26_data.xml")