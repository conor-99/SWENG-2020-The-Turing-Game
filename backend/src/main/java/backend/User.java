package backend;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class User
{
	int rank;
	String username;
	Double score;

	User(String username){
		this.rank = -1;
		this.username = username;
		this.score = 0.0;
	}

	User(String username, Double score){
		this.username = username;
		this.score = score;
	}
	
	User(int rank, String username, Double score){
		this.rank = rank;
		this.username = username;
		this.score = score;
	}

	public void setRank(int newRank) {
		rank = newRank;
	}

	public int getRank() {
		return rank;
	}

	public void setUserName(String newUserName) {
		username = newUserName;
	}

	public String getUserName() {
		return username;
	}

	public void setScore(Double newScore) {
		score = newScore;
	}

	public Double getScore() {
		return score;
	}
}

