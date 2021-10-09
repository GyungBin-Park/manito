var sale_1_compare_chart = document.getElementById("sale_compare_Chart1");
var sale_2_compare_chart = document.getElementById("sale_compare_Chart2");
var sale_3_compare_chart = document.getElementById("sale_compare_Chart3");

var test_num = sector_num

if ( test_num == 3 ){
var sale_compare_chart3 = new Chart(sale_3_compare_chart, {
        type: 'bar',
        data: {
            labels: compare_date,
            datasets: [{
                label: result_compare_list[0]['code_name'],
                data: result_compare_list[0]['sale'],
                backgroundColor : 'rgba(208, 163, 234, 1)',
                borderColor: 'rgba(208, 163, 234, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[1]['code_name'],
                data: result_compare_list[1]['sale'],
                backgroundColor: 'rgba(233, 85, 133, 1)',
                borderColor: 'rgba(233, 85, 133, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[2]['code_name'],
                data: result_compare_list[2]['sale'],
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




else if ( test_num == 2 ){
// 2개 sale
    var sale_compare_chart2 = new Chart(sale_2_compare_chart, {
        type: 'bar',
        data: {
            labels: compare_date,
            datasets: [{
                label: result_compare_list[0]['code_name'],
                data: result_compare_list[0]['sale'],
                backgroundColor: 'rgba(223, 183, 245, 1)',
                borderColor: 'rgba(223, 183, 245, 1)',
                borderWidth: 1,
                borderRadius : 10,
            },
            {
                label: result_compare_list[1]['code_name'],
                data: result_compare_list[1]['sale'],
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
//1개 - sale
var sale_compare_chart1 = new Chart(sale_1_compare_chart, {
    type: 'bar',
    data: {
        labels: compare_date,
        datasets: [{
            label: result_compare_list[0]['code_name'],
            data: result_compare_list[0]['sale'],
            backgroundColor: 'rgba(233, 85, 133,1)',
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




