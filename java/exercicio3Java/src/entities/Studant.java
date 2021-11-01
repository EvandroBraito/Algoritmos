package entities;

public class Studant {

	public String name;
	public double grade1;
	public double grade2;
	public double grade3;
	
	public double sumNotes() {
		return grade1 + grade2 + grade3;
	}
	
	public double missingPoints() {
		if(sumNotes() < 60.0) {
			return 60.0 - sumNotes();
		}
		else {
			return 0.0;
		}
	}
}
