$(document).ready(function() {
    $.ajax({
        url: '/chart-data',
        method: 'GET',
        success: function(data) {
            let ctx = document.getElementById('myChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Test Label',
                        data: data.values,
                        backgroundColor: 'rgba(75, 192,192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 0.2)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    });
});
