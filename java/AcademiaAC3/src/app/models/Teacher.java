package app.models;

public class Teacher extends Person {
	int id;
	double salary;

	public Teacher(String name, int age, float weight, float height, int id, double salary) {
		super(name, age, weight, height);
		this.id = id;
		this.salary = salary;
	}

	public Teacher() {
		
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	@Override
	public String toString() {
		return "Teacher [id=" + id + ", salary=" + salary + ", name=" + name + ", age=" + age + ", weight=" + weight
				+ ", height=" + height + "]";
	}
	
}
