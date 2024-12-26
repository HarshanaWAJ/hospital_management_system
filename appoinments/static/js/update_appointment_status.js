document.querySelectorAll('.accept-btn').forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();

        const appointmentId = this.getAttribute('data-id');  

        Swal.fire({
            title: 'Are you sure?',
            text: 'You want to accept this appointment?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Yes, accept it!',
            cancelButtonText: 'No, keep it as pending',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                // Make an AJAX request to accept the appointment
                fetch(`/appointments/accept_reject_appointment/${appointmentId}/accept/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => {
                    // Check if the response is successful (status 200 OK)
                    if (response.ok) {
                        return response.json(); // Parse JSON response
                    } else {
                        return Promise.reject('Failed to accept the appointment');
                    }
                })
                .then(data => {
                    if (data.success) {
                        Swal.fire('Accepted!', 'Your appointment has been accepted.', 'success');
                        // Refresh the page after a successful update
                        setTimeout(() => {
                            location.reload();
                        }, 1500); // Refresh after 1.5 seconds
                    } else {
                        Swal.fire('Error', 'There was an issue accepting the appointment.', 'error');
                    }
                })
                .catch(error => {
                    Swal.fire('Error', error, 'error');
                });
            }
        });
    });
});

document.querySelectorAll('.cancel-btn').forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();

        const appointmentId = this.getAttribute('data-id');  

        Swal.fire({
            title: 'Are you sure?',
            text: 'You want to reject this appointment?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Yes, reject it!',
            cancelButtonText: 'No, keep it as pending',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                // Make an AJAX request to reject the appointment
                fetch(`/appointments/accept_reject_appointment/${appointmentId}/reject/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => {
                    // Check if the response is successful (status 200 OK)
                    if (response.ok) {
                        return response.json(); // Parse JSON response
                    } else {
                        return Promise.reject('Failed to reject the appointment');
                    }
                })
                .then(data => {
                    if (data.success) {
                        Swal.fire('Rejected!', 'Your appointment has been rejected.', 'success');
                        // Refresh the page after a successful update
                        setTimeout(() => {
                            location.reload();
                        }, 1500); // Refresh after 1.5 seconds
                    } else {
                        Swal.fire('Error', 'There was an issue rejecting the appointment.', 'error');
                    }
                })
                .catch(error => {
                    Swal.fire('Error', error, 'error');
                });
            }
        });
    });
});
