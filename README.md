# AWS Restart Lessons

## Introduction
This repository contains the AWS Restart Lessons. Follow the instructions below to install and set up the project on your local machine.

## Installation

1. **Create a new folder** outside of all existing folders with git projects inside.

2. **Clone the project** into the new folder by running the following command in your terminal:
    ```sh
    git clone git@github.com:vmigel/aws-restart-lessons.git .
    ```

## SSH Key Setup

To connect your local computer to the repository, you need to generate an SSH key.

1. **Generate the SSH key** by running the following command:
    ```sh
    ssh-keygen
    ```

2. **Locate the public SSH key** on your file system. The default path is:
    ```
    C:\Users\your-user\.ssh\id_rsa.pub
    ```

3. **Open the public SSH key** with a text editor (e.g., vim or Notepad.exe) and copy the entire content of the file.

## Adding SSH Key to GitHub

1. Go to your GitHub account settings.

2. Navigate to `SSH and GPG keys`.

3. Click on `New SSH key`.

4. Paste the copied public key into the `Key` field and provide a suitable `Title`.

5. Click `Add SSH key` to save it.

## Usage

After setting up the SSH key, you should be able to pull changes to the repository without having to enter your GitHub credentials each time.

To puch changes please give me your github username or email. After I added you, you will receive email with activation link. After you 'activate' you will have posibility to push as well.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out to the repository owner.

---

Happy coding!
