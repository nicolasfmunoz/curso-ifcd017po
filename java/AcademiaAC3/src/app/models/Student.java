package app.models;

public class Student extends Person {
	int id;
	char classroom;
	public Student(String name, int age, float weight, float height, int id, char classroom) {
		super(name, age, weight, height);
		this.id = id;
		this.classroom = classroom;
	}
	
	public Student() {
		
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public char getClassroom() {
		return classroom;
	}

	public void setClassroom(char classroom) {
		this.classroom = classroom;
	}

	@Override
	public String toString() {
		return "Student [id=" + id + ", classroom=" + classroom + ", name=" + name + ", age=" + age + ", weight="
				+ weight + ", height=" + height + "]";
	}
	
	
}
