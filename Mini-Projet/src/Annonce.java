import java.util.*;

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
	
	public Annonce(String nom, String desc, int prix, Language lang, ArrayList<String> tags)
	{
		nom_ = nom;
		description_ = desc;
		prix_ = prix;
		lang_ = lang;
		tags_ = tags;
	}
	
}
