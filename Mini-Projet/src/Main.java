
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import java.util.*;
import java.util.Map.Entry;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		adsList = new HashMap<Integer, Annonce>();
		viewedAdsList = new ArrayList<Integer>();
		readXML();
		readViewedXML();
		createProfile();
		
		// Remove already viewed ads from ads db
		
		for(Integer adId: viewedAdsList)
		{
			if(adsList.get(adId) != null)
				adsList.remove(adId);
		}
	}
	
	private static void createProfile()
	{
		ArrayList<Annonce> viewedAds = new ArrayList<Annonce>();
		
		for(Integer curId: viewedAdsList)
		{
			viewedAds.add(adsList.get(curId));
		}
		
		userProfile_ = new Profil(viewedAds);
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
	
	private static void readViewedXML()
	{
		try
		{
			File adsFile = new File("viewedAds.xml");
			DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
			Document doc = dBuilder.parse(adsFile);
			
			doc.getDocumentElement().normalize();
			
			NodeList nAdList = doc.getElementsByTagName("ad");
			for(int i = 0; i < nAdList.getLength(); i++)
			{
				Element curElem = (Element)nAdList.item(i);
				viewedAdsList.add(Integer.parseInt(curElem.getAttribute("id")));
			}
		}
		
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	
	private static HashMap<Integer, Annonce> adsList;
	private static ArrayList<Integer> viewedAdsList;
	private static Profil userProfile_;

}
