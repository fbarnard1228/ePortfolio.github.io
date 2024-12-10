

public class Contact {
    // Needed variables for the class
    private String contactId;
    private String firstName;
    private String lastName;
    private String phone;
    private String address;
    
    // Constructor to create an object of the class and check them against requirements
    public Contact(String contactId, String firstName, String lastName, String phone, String address) {
        validateContactId(contactId);
        validateName(firstName, "First Name");
        validateName(lastName, "Last Name");
        validatePhone(phone);
        validateAddress(address);
        
        this.contactId = contactId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.address = address;
    }
    
    // Getter and setter methods
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
        validateName(fName, "First Name");
        this.firstName = fName;
    }
    public void setLastName(String lName) {
        validateName(lName, "Last Name");
        this.lastName = lName;
    }
    public void setPhone(String newNumber) {
        validatePhone(newNumber);
        this.phone = newNumber;
    }
    public void setAddress(String newAddress) {
        validateAddress(newAddress);
        this.address = newAddress;
    }

    // Validation methods
    private void validateContactId(String contactId) {
        if (contactId == null || contactId.length() > 10) {
            throw new IllegalArgumentException("Invalid ID: contactId must not be null and must be 10 characters or fewer.");
        }
    }

    private void validateName(String name, String fieldName) {
        if (name == null || name.length() > 10) {
            throw new IllegalArgumentException(fieldName + " should be no more than 10 characters.");
        }
    }

    private void validatePhone(String phone) {
        if (phone == null || phone.length() != 10) {
            throw new IllegalArgumentException("Phone Number should be exactly 10 characters.");
        }
    }

    private void validateAddress(String address) {
        if (address == null || address.length() > 30) {
            throw new IllegalArgumentException("Address should be no more than 30 characters.");
        }
    }
}
