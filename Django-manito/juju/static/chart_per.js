
var per_1_compare_chart = document.getElementById("per_compare_Chart1");
var per_2_compare_chart = document.getElementById("per_compare_Chart2");
var per_3_compare_chart = document.getElementById("per_compare_Chart3");

var test_num = sector_num

if ( test_num == 3 ){
// 3개 per
var per_compare_chart3 = new Chart(per_3_compare_chart, {
    type: 'bar',
    data: {
        labels: compare_date,
        datasets: [{
            label: result_compare_list[0]['code_name'],
            data: result_compare_list[0]['per'],
            backgroundColor : 'rgba(208, 163, 234, 1)',
            borderColor: 'rgba(208, 163, 234, 1)',
            borderWidth: 1,
            borderRadius : 10,
        },
        {
            label: result_compare_list[1]['code_name'],
            data: result_compare_list[1]['per'],
            backgroundColor: 'rgba(233, 85, 133, 1)',
            borderColor: 'rgba(233, 85, 133, 1)',
            borderWidth: 1,
            borderRadius : 10,
        },{
            label: result_compare_list[2]['code_name'],
            data: result_compare_list[2]['per'],
            backgroundColor: 'rgba(93, 200, 185, 1)',
            borderColor: 'rgba(93, 200, 185, 1)',
            borderWidth: 1,
            borderRadius : 10,
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

// 업종 내 종목 데이터가 2개일 경우
else if ( test_num == 2 ){
    var per_compare_chart2 = new Chart(per_2_compare_chart, {
    type: 'bar',
    data: {
        labels: compare_date,
        datasets: [{
            label: result_compare_list[0]['code_name'],
            data: result_compare_list[0]['per'],
            backgroundColor: 'rgba(223, 183, 245, 1)',
            borderColor: 'rgba(223, 183, 245, 1)',
            borderWidth: 1,
            borderRadius : 10,
        },
        {
            label: result_compare_list[1]['code_name'],
            data: result_compare_list[1]['per'],
            backgroundColor: 'rgba(110, 215, 200, 1)',
            borderColor: 'rgba(110, 215, 200, 1)',
            borderWidth: 1,
            borderRadius : 10,
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



else {
    var per_compare_chart1 = new Chart(per_1_compare_chart, {
    type: 'bar',
    data: {
        labels: compare_date,
        datasets: [{
            label: result_compare_list[0]['code_name'],
            data: result_compare_list[0]['per'],
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
