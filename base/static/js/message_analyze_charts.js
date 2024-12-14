document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('serviceQualityChart').getContext('2d');

    // Get data attributes for the percentages
    const positive = parseFloat(document.getElementById('serviceQualityChart').getAttribute('data-positive'));
    const negative = parseFloat(document.getElementById('serviceQualityChart').getAttribute('data-negative'));
    const neutral = parseFloat(document.getElementById('serviceQualityChart').getAttribute('data-neutral'));

    // Create chart
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                label: 'Service Quality Distribution',
                data: [positive, negative, neutral],
                backgroundColor: ['#4caf50', '#f44336', '#ffa500'],
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.raw.toFixed(2) + '%';
                        }
                    }
                },
                legend: {
                    position: 'top'
                }
            }
        }
    });
});