Task1: 
Step 6: Documentation
Authentication Documentation
1. Registration
URL: /register/

Description: Allows new users to create an account.

Fields: Username, email, password, confirm password.

Test: Fill out the form and submit. Verify the user is created and logged in.

2. Login
URL: /login/

Description: Allows existing users to log in.

Fields: Username, password.

Test: Log in with valid credentials. Verify the user is redirected to the profile page.

3. Logout
URL: /logout/

Description: Logs out the current user.

Test: Click the logout link. Verify the user is logged out and redirected to the home page.

4. Profile Management
URL: /profile/

Description: Allows authenticated users to view and edit their profile.

Fields: Bio, profile picture.

Test: Update the profile and verify the changes are saved.

5. Security
CSRF Protection: All forms include {% csrf_token %}.

Password Hashing: Passwords are securely hashed using Django’s built-in algorithms.

Authentication Decorators: Views like profile are protected with @login_required.