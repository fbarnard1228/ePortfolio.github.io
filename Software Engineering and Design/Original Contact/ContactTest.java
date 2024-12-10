import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;


class ContactTest {

	@Test
	void testContact() {
		var newContact = new Contact("1000", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getFirstName().equals("Farrik"));
		assertTrue(newContact.getLastName().equals("Barnard"));
		assertTrue(newContact.getContactId().equals("1000"));
		assertTrue(newContact.getPhone().equals("6096657878"));
		assertTrue(newContact.getAddress().equals("4011 Great Ln. Party, NJ 08754"));
	}
	// test for too long ID
	@Test
	void testContacIdMoreThanTen() {
		var newContact = new Contact("123456789010", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getContactId().equals("123456789010"));
	}
	
	@Test
	void testContacIdLessThanTen() {
		var newContact = new Contact("12345678", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getContactId().equals("12345678"));
	}
	
	@Test
	void testContacIdEqualThanTen() {
		var newContact = new Contact("1234567890", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getContactId().equals("1234567890"));
	}
	// test for null ID	
	@Test
	void testContacIdNull() {
		var newContact = new Contact(null, "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertNull(newContact.getContactId().equals(null));
	}
	// test for first name
	@Test
	void testContactFirstNameIsMoreThanTen() {
		var newContact = new Contact("10001", "Farrik23423423432", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getFirstName().equals("Farrik23423423432"));
	}
	
	@Test
	void testContactFirstNameIsLessThanTen() {
		var newContact = new Contact("10001", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getFirstName().equals("Farrik"));
	}
	
	@Test
	void testContactFirstNameIsEqualToTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getFirstName().equals("Farrik1234"));
	}
	// test for null first name
	@Test
	void testContactFirstNameNull() {
		var newContact = new Contact("1001", null, "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertNull(newContact.getFirstName().equals(null));
	}
	// test for last name
	@Test
	void testContactLastNameIsMoreThanTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard23423423432", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getLastName().equals("Barnard23423423432"));
	}
	
	@Test
	void testContactLastNameIsLessThanTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getLastName().equals("Barnard"));
	}
	
	@Test
	void testContactLastNameIsEqualToTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getLastName().equals("Barnard123"));
	}
	// test for null last name
	@Test
	void testContactClassLastNameNull() {
		var newContact = new Contact("10001", "Farrik1234", null, "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getLastName().equals(null));
	}
	// test for phone number
	@Test
	void testContactPhoneToEqualTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getPhone().equals("6096657878"));
	}
	
	@Test
	void testContactPhoneMoreThanTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878343", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getPhone().equals("6096657878343"));
	}
	
	@Test
	void testContactPhoneLessThanTen() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "609878", "4011 Great Ln. Party, NJ 08754");
		assertTrue(newContact.getPhone().equals("609878"));
	}
	// test for null phone
	@Test
	void testContactPhoneNull() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", null, "4011 Great Ln. Party, NJ 08754");
		assertNull(newContact.getPhone().equals(null));
	}
	// test address
	@Test
	void testContactAddressMoreThanThirty() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754 23423423432");
		assertTrue(newContact.getAddress().equals("4011 Great Ln. Party, NJ 087544355235255235"));
	}
	
	void testContactAddressLessThanThirty() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754 23423423432");
		assertTrue(newContact.getAddress().equals("4011 Great Ln. Party 08754"));
	}
	
	void testContactAddressEqualToThirty() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754 23423423432");
		assertTrue(newContact.getAddress().equals("4011 Great Ln. Party, NJ 08754"));
	}
	// test for null address
	@Test
	void testContactClassAddressnull() {
		var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", null);
		assertTrue(newContact.getAddress().equals(null));
	}
}