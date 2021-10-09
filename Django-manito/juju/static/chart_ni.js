var ni_1_compare_chart = document.getElementById("ni_compare_Chart1");
var ni_2_compare_chart = document.getElementById("ni_compare_Chart2");
var ni_3_compare_chart = document.getElementById("ni_compare_Chart3");

var test_num = sector_num

// 3개 종목 Ni
if ( test_num == 3 ){
var ni_compare_chart3 = new Chart(ni_3_compare_chart, {
        type: 'bar',
        data: {
            labels: compare_date,
            datasets: [{
                label: result_compare_list[0]['code_name'],
                data: result_compare_list[0]['ni'],
                backgroundColor : 'rgba(208, 163, 234, 1)',
                borderColor: 'rgba(208, 163, 234, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[1]['code_name'],
                data: result_compare_list[1]['ni'],
                backgroundColor: 'rgba(233, 85, 133, 1)',
                borderColor: 'rgba(233, 85, 133, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[2]['code_name'],
                data: result_compare_list[2]['ni'],
                backgroundColor: 'rgba(93, 200, 185, 1)',
                borderColor: 'rgba(93, 200, 185, 1)',
                borderWidth: 1,
                borderRadius : 10,
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        font: {
                            size: 14,
                        }
                   },
                },
            },
            scales: {
                x: {
                display: true,
                position: 'bottom',
                grid: {
                    display : false
                    }
                },

                y: {
                    beginAtZero: true,
                    type: 'linear',
                    display: false,
                    position: 'right',
                    grid: {
                        display : false
                    },
                }
            }
        }
    });

}



// 2개 종목 Ni
else if ( test_num == 2 ){
    var ni_compare_chart2 = new Chart(ni_2_compare_chart, {
        type: 'bar',
        data: {
            labels: compare_date,
            datasets: [{
                label: result_compare_list[0]['code_name'],
                data: result_compare_list[0]['ni'],
                backgroundColor : 'rgba(223, 183, 245, 1)',
                borderColor: 'rgba(223, 183, 245, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[1]['code_name'],
                data: result_compare_list[1]['ni'],
                backgroundColor: 'rgba(110, 215, 200, 1)',
                borderColor: 'rgba(110, 215, 200, 1)',
                borderWidth: 1,
                borderRadius : 10,
            }]
        },
        options: {
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        font: {
                            size: 14,
                        }
                   },
                },
            },
            scales: {
                x: {
                display: true,
                position: 'bottom',
                grid: {
                    display : false
                    }
                },

                y: {
                    beginAtZero: true,
                    type: 'linear',
                    display: false,
                    position: 'right',
                    grid: {
                        display : false
                    },
                }
            }
        }
    });
}
else{
//1개 - ni
var ni_compare_chart1 = new Chart(ni_1_compare_chart, {
    type: 'bar',
    data: {
        labels: compare_date,
        datasets: [{
            label: result_compare_list[0]['code_name'],
            data: result_compare_list[0]['ni'],
            backgroundColor:'rgba(233, 85, 133,1)',
            borderColor: 'rgba(233, 85, 133,1)',
            borderWidth: 1,
            borderRadius : 10,
            barPercentage: 0.5,
        }
        ]
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    font: {
                        size: 14,
                    }
                },
            },
        },
        scales: {
            x: {
                display: true,
                position: 'bottom',
                grid: {
                    display : false
                    }
                },

                y: {
                    beginAtZero: true,
                    type: 'linear',
                    display: false,
                    position: 'right',
                    grid: {
                        display : false
                    },
                }
        }
    }
});
}




