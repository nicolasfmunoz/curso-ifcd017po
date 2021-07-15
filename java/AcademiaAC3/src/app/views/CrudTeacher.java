package app.views;

import java.util.Hashtable;
import java.util.List;
import java.util.Scanner;

import app.models.Student;


public class CrudTeacher {
	static Scanner sc = new Scanner(System.in);
	
	public List<Student> createStudent(List<Student> student_list) {
		String[] field_names = {"name", "age", "weight", "height", "classroom", "id"};
		
		Hashtable<String, String> fields = new Hashtable<>();
		
		// poco eficiente
		for (String f : field_names) {			
			System.out.println(String.format("Introduzca %s: ", f));
			String input = sc.next();
			
			fields.put(f, input);
		}

		Student student = new Student();
		
		student.setName(fields.get("name"));
		student.setAge(Integer.parseInt(fields.get("age")));
		student.setWeight(Float.parseFloat(fields.get("weight")));
		student.setHeight(Float.parseFloat(fields.get("height")));
		student.setClassroom(fields.get("classroom").charAt(0));
		student.setId(Integer.parseInt(fields.get("id")));

		student_list.add(student);
		
		return student_list;
	}
	
	public void readAllStudents(List<Student> student_list) {
		
	}
	
	public void readStudent(List<Student> student_list, int student_id) {
		
	}
	
	public List<Student> updateStudent(List<Student> student_list) {
		return student_list;
	}
	
	public void deleteStudent(List<Student> student_list, int student_id) {
		
	}

}
