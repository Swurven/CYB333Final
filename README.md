# Password Strength Analyzer

## Project Overview

The Password Strength Analyzer is a Python-based tool designed to evaluate the strength of passwords and provide actionable feedback to improve security. This tool aligns with established security standards, including guidelines from the **National Institute of Standards and Technology (NIST)** and the **Open Web Application Security Project (OWASP)**. By focusing on practical and research-based password policies, the analyzer emphasizes strong, memorable, and secure password practices.

## Features

- **Minimum Password Length:** Requires a minimum of 8 characters to align with NIST standards.
- **Passphrase Support:** Encourages longer passphrases up to 64 characters, supporting the inclusion of spaces for better memorability.
- **Character Diversity:** Offers feedback encouraging a mix of lowercase, uppercase, numbers, and special characters, while avoiding mandatory complexity rules that may frustrate users.
- **Actionable Feedback:** Provides clear suggestions to improve password strength if weaknesses are detected.
- **Dynamic Scoring:** Evaluates password strength as "Weak," "Moderate," or "Strong" based on various factors, such as length, character variety, and passphrase features.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<Swurven>/password-strength-analyzer.git
   cd password-strength-analyzer
   ```
2. Run the script:
   ```bash
   python password_analyzer.py
   ```
3. Enter a password to analyze. The tool will provide its strength and offer suggestions for improvement if needed.

### Example

```bash
Enter a password to analyze: secure password123
Password Strength: Moderate
Feedback:
- Consider adding a mix of letters, numbers, and special characters for stronger security.
```

## Security Guidelines

This tool is built based on the following guidelines:

- **NIST SP 800-63B:** Emphasizes minimum password length and encourages passphrases for better security and usability.
- **OWASP Authentication Cheat Sheet:** Recommends allowing a wide range of characters, including spaces, and enforcing sensible length constraints.

## Contribution

We welcome contributions to enhance this tool! If you have suggestions or improvements:

1. Fork this repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

## AI Assistance

This project was developed with the help of GitHub Copilot. AI suggestions were instrumental in structuring functions and improving code quality. To ensure understanding, the code was extensively tested and refined based on research and feedback.

## Reflection

Developing this analyzer was a learning experience in understanding password security best practices. Incorporating established standards like NIST and OWASP helped build a tool that prioritizes both usability and security.

## Acknowledgments

This project was developed as part of a security automation class. Special thanks to GitHub Copilot for assisting with the development process.

Replace `<Swurven>` with your GitHub username and include any additional acknowledgments or details relevant to your project. Let me know if you'd like assistance uploading this to your repository!
