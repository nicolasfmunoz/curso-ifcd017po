package app.models;

public class Person {
	public String name;
	public int age;
	public float weight;
	public float height;
	
	
	public Person(String name, int age, float weight, float height) {
		super();
		this.name = name;
		this.age = age;
		this.weight = weight;
		this.height = height;
	}


	public Person() {
		super();
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public int getAge() {
		return age;
	}


	public void setAge(int age) {
		this.age = age;
	}


	public float getWeight() {
		return weight;
	}


	public void setWeight(float weight) {
		this.weight = weight;
	}


	public float getHeight() {
		return height;
	}


	public void setHeight(float height) {
		this.height = height;
	}

	@Override
	public String toString() {
		return "Persona [name=" + name + ", age=" + age + ", weight=" + weight + ", height=" + height + "]";
	}
	
	
}
