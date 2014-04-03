import java.util.*;
import java.util.Map.Entry;

// Représente le profil de l'utilisateur

public class Profil {
	public HashMap<String, Integer> tokens;
	
	public Profil(ArrayList<Annonce> viewedAds)
	{
		tokens = new HashMap<String, Integer>();
		for(Annonce ad : viewedAds)
		{
			ArrayList<String> curTokens = new ArrayList<String>();
			curTokens.addAll(TokenParser.parseString(ad.nom_));
			curTokens.addAll(TokenParser.parseString(ad.description_));
			
			for(String str: curTokens)
			{
				if(tokens.get(str) == null)
					tokens.put(str,1);
				else
					tokens.put(str, tokens.get(str) + 1);
			}
			
			for(String str: ad.tags_)
			{
				if(tokens.get(str) == null)
					tokens.put(str,2);
				else
					tokens.put(str, tokens.get(str) + 2);
			}
		}
	}
}
