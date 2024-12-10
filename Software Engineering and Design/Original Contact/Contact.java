

public class Contact {
	// needed variables for the class
	private String contactId;
	private String firstName;
	private String lastName;
	private String phone;
	private String address;
	
	
	
	// create an object of the class and check them against requirements
	public Contact(String contactId, String firstName, String lastName, String phone, String address) {
		
		if (contactId == null || contactId.length() > 10) {
			throw new IllegalArgumentException("Invalid ID");
		}
		
		if (firstName == null || firstName.length() > 10) {
			throw new IllegalArgumentException("First Name should be no more than 10.");
		}
		
		if (lastName == null || lastName.length() > 10) {
			throw new IllegalArgumentException("Last Name should be no more than 10.");
		}
		
		if (phone == null || phone.length() != 10) {
			throw new IllegalArgumentException("Phone Number should be no more than 10.");
		}
		
		if (address == null || address.length() > 30) {
			throw new IllegalArgumentException("Address should be no more than 30.");
		}
		
		this.contactId = contactId;
		this.firstName = firstName;
		this.lastName = lastName;
		this.phone = phone;
		this.address = address;
	}
	
	// getter and setter methods
	public String getContactId() {
		return contactId;
	}
	public String getFirstName() {
		return firstName;
	}
	public String getLastName() {
		return lastName;
	}
	public String getPhone() {
		return phone;
	}
	public String getAddress() {
		return address;
	}

	public void setFirstName(String fName) {
		if (fName == null || fName.length() > 10) {
			throw new IllegalArgumentException("First Name should be no more than 10.");
		}
		this.firstName = fName;
	}
	public void setLastName(String lName) {
		if (lName == null || lName.length() > 10) {
			throw new IllegalArgumentException("Last Name should be no more than 10.");
		}
		this.lastName = lName;
	}
	public void setPhone(String newNumber) {
		if (newNumber == null || newNumber.length() != 10) {
			throw new IllegalArgumentException("Phone Number should be no more than 10.");
		}
		this.phone = newNumber;
	}
	public void setAddress(String newAddress) {
		if (newAddress == null || newAddress.length() > 30) {
			throw new IllegalArgumentException("Address should be no more than 30.");
		}
		this.address = newAddress;
	}
}