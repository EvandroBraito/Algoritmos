package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Studant;

public class Program {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		double note1, note2, note3;
		
		System.out.println("Inform the notes: ");
		
		Studant studant = new Studant();
		
		studant.name = sc.nextLine();
		studant.grade1 = sc.nextDouble();
		studant.grade2 = sc.nextDouble();
		studant.grade3 = sc.nextDouble();

		System.out.printf("Final grade: %.2f%n", studant.sumNotes());
		
		if(studant.sumNotes() < 60.0) {
			System.out.println("FAILED");
			System.out.printf("MISSING %.2f POINTS%n", studant.missingPoints());
		}
		else {
			System.out.println("PASS");
		}
	}

}
