package app.control;

import java.util.ArrayList;
import java.util.List;

import app.models.Student;
import app.views.CrudTeacher;

public class AppMain {

	public static void main(String[] args) {
		CrudTeacher crud = new CrudTeacher();
		
		List<Student> list = new ArrayList<Student>();
		
		List<Student> new_list = crud.createStudent(list);
	}

}
