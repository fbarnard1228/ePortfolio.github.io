import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class ContactTest {

    @Test
    void testContact() {
        // Test for valid input
        var newContact = new Contact("1000", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("Farrik", newContact.getFirstName());
        assertEquals("Barnard", newContact.getLastName());
        assertEquals("1000", newContact.getContactId());
        assertEquals("6096657878", newContact.getPhone());
        assertEquals("4011 Great Ln. Party, NJ 08754", newContact.getAddress());
    }

    // Test for too long ID
    @Test
    void testContactIdMoreThanTen() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("123456789010", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    @Test
    void testContactIdLessThanTen() {
        var newContact = new Contact("12345678", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("12345678", newContact.getContactId());
    }

    @Test
    void testContactIdEqualToTen() {
        var newContact = new Contact("1234567890", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("1234567890", newContact.getContactId());
    }

    // Test for null ID
    @Test
    void testContactIdNull() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact(null, "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    // Test for first name
    @Test
    void testContactFirstNameMoreThanTen() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik23423423432", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    @Test
    void testContactFirstNameLessThanTen() {
        var newContact = new Contact("10001", "Farrik", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("Farrik", newContact.getFirstName());
    }

    @Test
    void testContactFirstNameEqualToTen() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("Farrik1234", newContact.getFirstName());
    }

    // Test for null first name
    @Test
    void testContactFirstNameNull() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("1001", null, "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    // Test for last name
    @Test
    void testContactLastNameMoreThanTen() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard23423423432", "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    @Test
    void testContactLastNameLessThanTen() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("Barnard", newContact.getLastName());
    }

    @Test
    void testContactLastNameEqualToTen() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("Barnard123", newContact.getLastName());
    }

    // Test for null last name
    @Test
    void testContactLastNameNull() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", null, "6096657878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    // Test for phone number
    @Test
    void testContactPhoneEqualToTen() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("6096657878", newContact.getPhone());
    }

    @Test
    void testContactPhoneMoreThanTen() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard123", "6096657878343", "4011 Great Ln. Party, NJ 08754");
        });
    }

    @Test
    void testContactPhoneLessThanTen() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard123", "609878", "4011 Great Ln. Party, NJ 08754");
        });
    }

    // Test for null phone
    @Test
    void testContactPhoneNull() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard123", null, "4011 Great Ln. Party, NJ 08754");
        });
    }

    // Test for address
    @Test
    void testContactAddressMoreThanThirty() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754 23423423432");
        });
    }

    @Test
    void testContactAddressLessThanThirty() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("4011 Great Ln. Party, NJ 08754", newContact.getAddress());
    }

    @Test
    void testContactAddressEqualToThirty() {
        var newContact = new Contact("10001", "Farrik1234", "Barnard123", "6096657878", "4011 Great Ln. Party, NJ 08754");
        assertEquals("4011 Great Ln. Party, NJ 08754", newContact.getAddress());
    }

    // Test for null address
    @Test
    void testContactAddressNull() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("10001", "Farrik1234", "Barnard123", "6096657878", null);
        });
    }
}
