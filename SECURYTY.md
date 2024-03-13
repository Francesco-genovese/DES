# Security Policy

## Supported Versions

Use this section to inform users about the versions of your project currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 0.9.x   | :x:                |

## Reporting a Vulnerability

Use this section to guide users on how to report a vulnerability.

- **Where to Report:** Create an issue on the project's GitHub repository.
- **Response Time:** You can expect an initial response within 48 hours.
- **Updates:** Regular updates will be provided on the progress of addressing the reported vulnerability.
- **Vulnerability Acceptance/Decline:** The team will assess the reported vulnerability and inform the reporter of whether it is accepted or declined, providing reasons for the decision.

## Encryption Algorithm (DES) Considerations

Ensure to understand the following considerations when using the DES encryption algorithm in this project:

1. **Key Security:**
   - The DES key is generated randomly with `get_random_bytes(8)`.
   - Consider using a more secure key generation method for critical applications.

2. **Encryption Mode:**
   - The program uses `DES.MODE_ECB`, which may not be secure for all purposes.
   - For enhanced security, consider using advanced encryption modes like Cipher Block Chaining (CBC).

3. **Key Input:**
   - When entering the key during decryption, ensure it is provided exactly as generated (8 characters).

4. **Security Awareness:**
   - Users are encouraged to be aware of the security implications and use this encryption responsibly.

Feel free to customize the information based on your specific project and security practices.
