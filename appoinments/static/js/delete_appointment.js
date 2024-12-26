document.querySelectorAll('.cancel-btn').forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();

        const recordId = this.getAttribute('data-id');  
        console.log(recordId);

        // Use SweetAlert2 for confirmation before deletion
        Swal.fire({
            title: 'Are you sure?',
            text: 'This action cannot be undone!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'No, keep it',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                // Proceed with the deletion if confirmed
                fetch(`/appointments/delete_appointment/${recordId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value  // Ensure CSRF token is included
                    }
                })
                .then(response => {
                    if (response.ok) {
                        // Show a success alert with SweetAlert2 and reload the page
                        Swal.fire({
                            title: 'Deleted!',
                            text: 'Your Appointment Canceled Successfully!',
                            icon: 'success'
                        }).then(() => {
                            location.reload();
                        });
                    } else {
                        Swal.fire({
                            title: 'Error!',
                            text: 'There was an issue deleting the record. Please try again.',
                            icon: 'error'
                        });
                    }
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                    Swal.fire({
                        title: 'Error!',
                        text: 'An unexpected error occurred. Please try again.',
                        icon: 'error'
                    });
                });
            } else {
                // User canceled the deletion
                Swal.fire({
                    title: 'Cancelled',
                    text: 'Your appointment is not canceled :)',
                    icon: 'info'
                });
            }
        });
    });
});
