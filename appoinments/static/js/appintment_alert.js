document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const success = urlParams.get('success');
    const error = urlParams.get('error');

    if (success) {
        // Display the success message using SweetAlert2
        Swal.fire({
            icon: 'success',
            title: 'Success!',
            text: 'Your Appointment Has Been Booked',
            showConfirmButton: true,
            timer: 3000  // Auto close after 3 seconds
        }).then(() => {
            // Clear the URL query parameters after the message is shown
            window.location.href = "home"; 
        });
    } else if (error) {
        // Display the error message using SweetAlert2
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'There was an error while booking your appointment.',
            showConfirmButton: true
        });
    }
});
