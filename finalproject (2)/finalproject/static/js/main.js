// // Select the "Already have an account?" link
// const alreadyHaveAccountLink = document.querySelector("#alreadyHaveAccountLink");

// // On page refresh, show the login form
// window.onload = () => {
//     // Simulate click on the login button and set action to "login"
//     setFormAction("login");
// };

// // Variable Declaration
// const loginBtn = document.querySelector("#login");
// const registerBtn = document.querySelector("#register");
// const loginForm = document.querySelector(".login-form");
// const registerForm = document.querySelector(".register-form");

// // Login button function
// loginBtn.addEventListener('click', () => {
//     // Set background color for active button
//     loginBtn.style.backgroundColor = "#21264D";
//     registerBtn.style.backgroundColor = "rgba(255,255,255,0.2)";

//     // Move forms and adjust opacity
//     loginForm.style.left = "50%";
//     registerForm.style.left = "-50%";
//     loginForm.style.opacity = 1;
//     registerForm.style.opacity = 0;

//     // Adjust border radius
//     document.querySelector(".col-1").style.borderRadius = "0 30% 20% 0";

//     // Set action to "login"
//     setFormAction("login");
// });

// // Register button function
// registerBtn.addEventListener('click', () => {
//     // Set background color for active button
//     loginBtn.style.backgroundColor = "rgba(255,255,255,0.2)";
//     registerBtn.style.backgroundColor = "#21264D";

//     // Move forms and adjust opacity
//     loginForm.style.left = "150%";
//     registerForm.style.left = "50%";
//     loginForm.style.opacity = 0;
//     registerForm.style.opacity = 1;

//     // Adjust border radius
//     document.querySelector(".col-1").style.borderRadius = "0 20% 30% 0";

//     // Set action to "signup"
//     setFormAction("signup");
// });

// // Function to set form action
// function setFormAction(action) {
//     const formAction = document.getElementById("formAction");
//     if (formAction) {
//         formAction.value = action;
//     }
// }

// // Event listener for "Already have an account?" link
// if (alreadyHaveAccountLink) {
//     alreadyHaveAccountLink.addEventListener('click', () => {
//         // Trigger a click on the login button when the link is clicked
//         loginBtn.click();
//     });
// }


// // Select the "Already have an account?" link
// const alreadyHaveAccountLink = document.querySelector("#alreadyHaveAccountLink");

// // Function to set up the login form
// function setupLoginForm() {
//     // Simulate click on the login button and set action to "login"
//     setFormAction("login");
// }

// // Variable Declaration
// const loginBtn = document.querySelector("#login");
// const registerBtn = document.querySelector("#register");
// const loginForm = document.querySelector(".login-form");
// const registerForm = document.querySelector(".register-form");

// // Login button function
// loginBtn.addEventListener('click', () => {
//     // Set background color for active button
//     loginBtn.style.backgroundColor = "#21264D";
//     registerBtn.style.backgroundColor = "rgba(255,255,255,0.2)";

//     // Move forms and adjust opacity
//     loginForm.style.left = "50%";
//     registerForm.style.left = "-50%";
//     loginForm.style.opacity = 1;
//     registerForm.style.opacity = 0;

//     // Adjust border radius
//     document.querySelector(".col-1").style.borderRadius = "0 30% 20% 0";

//     // Set action to "login"
//     setFormAction("login");
// });

// // Register button function
// registerBtn.addEventListener('click', () => {
//     // Set background color for active button
//     loginBtn.style.backgroundColor = "rgba(255,255,255,0.2)";
//     registerBtn.style.backgroundColor = "#21264D";

//     // Move forms and adjust opacity
//     loginForm.style.left = "150%";
//     registerForm.style.left = "50%";
//     loginForm.style.opacity = 0;
//     registerForm.style.opacity = 1;

//     // Adjust border radius
//     document.querySelector(".col-1").style.borderRadius = "0 20% 30% 0";

//     // Set action to "signup"
//     setFormAction("signup");
// });

// // Function to set form action
// function setFormAction(action) {
//     const formAction = document.getElementById("formAction");
//     if (formAction) {
//         formAction.value = action;
//     }
// }

// // Event listener for "Already have an account?" link
// if (alreadyHaveAccountLink) {
//     alreadyHaveAccountLink.addEventListener('click', () => {
//         // Trigger a click on the login button when the link is clicked
//         loginBtn.click();
//     });
// }

// // Call the setupLoginForm function when the JavaScript file is loaded
// setupLoginForm();


// On page load, show the login form and hide the registration form
window.onload = () => {
    showLoginForm();
};

// Variable Declaration
const loginBtn = document.querySelector("#login");
const registerBtn = document.querySelector("#register");

// Function to show the login form and hide the registration form
function showLoginForm() {
    loginBtn.style.backgroundColor = "#21264D";
    registerBtn.style.backgroundColor = "rgba(255,255,255,0.2)";

    document.querySelector(".login-form").style.left = "50%";
    document.querySelector(".register-form").style.left = "-50%";
    document.querySelector(".login-form").style.opacity = 1;
    document.querySelector(".register-form").style.opacity = 0;

    document.querySelector(".col-1").style.borderRadius = "0 30% 20% 0";

    setFormAction("login");
}

// Function to show the registration form and hide the login form
function showRegistrationForm() {
    loginBtn.style.backgroundColor = "rgba(255,255,255,0.2)";
    registerBtn.style.backgroundColor = "#21264D";

    document.querySelector(".login-form").style.left = "150%";
    document.querySelector(".register-form").style.left = "50%";
    document.querySelector(".login-form").style.opacity = 0;
    document.querySelector(".register-form").style.opacity = 1;

    document.querySelector(".col-1").style.borderRadius = "0 20% 30% 0";

    setFormAction("signup");
}

// Function to set form action
function setFormAction(action) {
    const formAction = document.getElementById("formAction");
    if (formAction) {
        formAction.value = action;
    }
}

// Event listener for login button
loginBtn.addEventListener('click', () => {
    showLoginForm();
});

// Event listener for register button
registerBtn.addEventListener('click', () => {
    showRegistrationForm();
});

// Event listener for "Already have an account?" link
const alreadyHaveAccountLink = document.querySelector("#alreadyHaveAccountLink");
if (alreadyHaveAccountLink) {
    alreadyHaveAccountLink.addEventListener('click', () => {
        showLoginForm(); // Show the login form when the link is clicked
    });
}

// Select the "Forgot Password?" link
const forgotPasswordLink = document.querySelector("#forgotPasswordLink");
if (forgotPasswordLink) {
    forgotPasswordLink.addEventListener('click', () => {
        // Show password reset form
        passwordResetForm.style.display = "block";

        // Hide other forms
        loginForm.style.opacity = 0;
        registerForm.style.opacity = 0;
    });
}
