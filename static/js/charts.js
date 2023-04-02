console.log("Hello from chart.js")


const chart_president = document.getElementById('chart-president');
          
    new Chart(chart_president, {
        type: 'bar',
        data: {
        labels: [{% for candidate in presidential_candidates.get_candidate %} '{{candidate.fullname}}', {% endfor %} ],
        datasets: [{
            label: '{{position_list|first}}',
            data: [{% for candidate in presidential_candidates.get_candidate %} {{candidate.polls}}, {% endfor %}],
            borderWidth: 2,
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

const chart_financial = document.getElementById('chart-financial');

new Chart(chart_financial, {
    type: 'bar',
    data: {
    labels: [{% for candidate in financial_candidates.get_candidate %} '{{candidate.fullname}}', {% endfor %}],
    datasets: [{
        label: 'Financial Secretary',
        data: [{% for candidate in financial_candidates.get_candidate %} {{candidate.polls}}, {% endfor %}],
        borderWidth: 2,
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


const chart_commissioner = document.getElementById('chart-commissioner');

new Chart(chart_commissioner, {
    type: 'bar',
    data: {
    labels: [{% for candidate in women_commissioner_candidates.get_candidate %} '{{candidate.fullname}}', {% endfor %}],
    datasets: [{
        label: '{{position_list|last}}',
        data: [{% for candidate in women_commissioner_candidates.get_candidate %} {{candidate.polls}}, {% endfor %}],
        borderWidth: 2,
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

