import java.util.*;
import java.lang.Math.*;

public class Annonce {
	
	public enum Language
	{
		FR, EN
	}
	
	public String nom_;
	public String description_;
	public int prix_;
	public Language lang_;
	public ArrayList<String> tags_;
	
	public float score;
	
	public Annonce(String nom, String desc, int prix, Language lang, ArrayList<String> tags)
	{
		nom_ = nom;
		description_ = desc;
		prix_ = prix;
		lang_ = lang;
		tags_ = tags;
		score = 0;
	}
	
	// Actuellement le score est calculé avec une correspondance token = 1 de score
	// Autrement dit, c'est (occurrences dans annonce) * (score dans profil).
	// C'est peut-être trop, il faudrait peut-être éliminer les doublons
	public void computeScore(Profil userProfile, ArrayList<Annonce> viewedAds)
	{
		// First add the score of every token encountered in this ad and viewedAds
		ArrayList<String> tokens = new ArrayList<String>();
		tokens.addAll(TokenParser.parseString(nom_));
		tokens.addAll(TokenParser.parseString(description_));
		
		int totalTokens = 0;
		
		for(String str : tokens)
		{
			if(userProfile.tokens.containsKey(str))
			{
				score += userProfile.tokens.get(str);
				totalTokens++;
			}
		}
		
		
		// Ajout du score pour le prix
		// Ce score est modulé de façon logarithmique par 
		// la correspondance en tokens
		
		float tokenScore = score;
		for(Annonce ad: viewedAds)
		{
			score += Math.log(1+tokenScore*0.1) * (totalTokens/tokens.size())*2;
		}
		
		
		// Ajout de score pour la langue
		for(Annonce ad: viewedAds)
		{
			if(lang_ == ad.lang_)
				score += 3*TokenParser.tokenScore;
		}
	}
	
}
