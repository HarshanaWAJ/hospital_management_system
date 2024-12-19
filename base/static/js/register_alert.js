// Function to show SweetAlert success message
function showSuccessAlert(message) {
    Swal.fire({
      icon: 'success',
      title: 'Success!',
      text: message,
      showConfirmButton: false,
      timer: 1500
    });
  }
  
  // Function to show SweetAlert error message
  function showErrorAlert(message) {
    Swal.fire({
      icon: 'error',
      title: 'Error!',
      text: message,
      showConfirmButton: true
    });
  }
  
  // Check if there's a success or error message passed from Django to display the alert
  document.addEventListener("DOMContentLoaded", function() {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
  
    if (successMessage) {
      showSuccessAlert(successMessage.innerText);
    }
  
    if (errorMessage) {
      showErrorAlert(errorMessage.innerText);
    }
  });
  