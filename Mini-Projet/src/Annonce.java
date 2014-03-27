import java.util.*;

public class Annonce {
	
	public enum Language
	{
		FR, EN
	}
	
	public String nom;
	public String description;
	public int prix;
	Language lang;
	List<String> tags;
	
}
