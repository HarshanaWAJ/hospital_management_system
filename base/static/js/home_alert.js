// Check if success or error flag is present in the URL
document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const success = urlParams.get('success');
    const error = urlParams.get('error');

    if (success) {
        Swal.fire({
            icon: 'success',
            title: 'Success!',
            text: 'Your message has been sent successfully.',
            showConfirmButton: false,
            timer: 3000
        });
    } else if (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'There was an error while sending your message.',
            showConfirmButton: true
        });
    }
});
