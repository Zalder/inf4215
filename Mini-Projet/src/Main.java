
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import java.util.*;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		adsList = new HashMap<Integer, Annonce>();
		readXML();

	}
	
	private static void readXML()
	{
		try
		{
			File adsFile = new File("ads.xml");
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(adsFile);
			
			doc.getDocumentElement().normalize();
			
			NodeList nAdList = doc.getElementsByTagName("ad");
			
			for(int i = 0; i < nAdList.getLength(); i++)
			{
				Node curNode = nAdList.item(i);
				
				if(curNode.getNodeType() == Node.ELEMENT_NODE)
				{
					Element curElement = (Element) curNode;
					
					int id = Integer.parseInt(curElement.getAttribute("id"));
					int prix = Integer.parseInt(curElement.getAttribute("prix"));
					String lang = curElement.getAttribute("lang");
					String name = curElement.getElementsByTagName("name").item(0).getTextContent();
					String desc = curElement.getElementsByTagName("desc").item(0).getTextContent();
					
					Element tags = (Element) curElement.getElementsByTagName("tags").item(0);
					NodeList tagList = tags.getElementsByTagName("tag");
					ArrayList<String> sTagList = new ArrayList<String>();
					
					for(int j = 0; j < tagList.getLength(); j++)
					{
						sTagList.add(tagList.item(j).getTextContent());
					}
					Annonce test = new Annonce(name, desc, prix, Annonce.Language.valueOf(lang), sTagList);
					adsList.put(id, test);
					
				}
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
			
	}
	
	private static HashMap<Integer, Annonce> adsList;

}
