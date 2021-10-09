// 종목 레포트 period chart

var day1_line = document.getElementById('day1_LineChart').getContext('2d');



// 종목의 1주일 ~ 1년 Period 차트
// day1_line 도 추가해야 함
var day7_line = document.getElementById('day7_LineChart').getContext('2d');
var month1_line = document.getElementById('month1_LineChart').getContext('2d');
var month3_line = document.getElementById('month3_LineChart').getContext('2d');
var year1_line = document.getElementById('year1_LineChart').getContext('2d');



const skipped = (ctx, value) => ctx.p0.skip || ctx.p1.skip ? value : undefined;
const down = (ctx, value) => ctx.p0.parsed.y > ctx.p1.parsed.y ? value : undefined;

// 1일 차트
var day1_Chart = new Chart(day1_line, {
    data: {
        labels: day1_list[0],
        datasets: [{
            type: 'line',
            label: '1일 시가',
            data: day1_list[1],
            pointStyle: 'dash',
//            backgroundColor: 'rgba(30, 144, 255, 1)',
            borderColor: 'rgba(30, 144, 255, 1)',
            segment: {
                borderColor: ctx => skipped(ctx, 'rgb(30, 144, 255, 0.2)') || down(ctx, 'rgb(255, 0, 0, 1)'),
                borderDash: ctx => skipped(ctx, [6, 6]),
            },
            borderWidth : 5,  // 선 두께
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: false, // 정적 동적 크기 변경?
        legend: false, //범례 표시 안함
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: { //마우스를 근처에 가져갔을 때, 데이터 값 표시
            mode: 'nearest',
            intersect: true
        },
        scales:{
            x: {
                display: true,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'left',
                suggestedMin: day1_list[4] - day1_list[4] * 0.1,
                suggestedMax: day1_list[3] + day1_list[3] * 0.05,
                grid: {
                    display : false
                },
            },
        }
    }
});












// 1주일 차트
// line, bar mix
var day7_LineChart = new Chart(day7_line, {
    data: {
        labels: day7_list[0],
        datasets: [{
            type: 'line',
            label: '7일 종가',
            data: day7_list[1],
            pointStyle: 'dash',
            backgroundColor: 'rgba(253, 126, 20, 1)',
            borderColor: 'rgba(253, 126, 20, 1)',
            yAxisID : 'y',
        },{
            type: 'bar',
            label: '7일 거래량',
            data: day7_list[2],
            backgroundColor: 'rgba(117, 183, 152, 1)',
            borderColor: 'rgba(117, 183, 152, 1)',
            barPercentage: 1,
            yAxisID : 'y2',
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: false, // 정적 동적 크기 변경?
        legend: false, //범례 표시 안함
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: { //마우스를 근처에 가져갔을 때, 데이터 값 표시
            mode: 'nearest',
            intersect: true
        },
        scales:{
            x: {
                display: false,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'left',
                suggestedMin: Math.min.apply(null, day7_list[1]) - Math.min.apply(null, day7_list[1]) * 0.1,
                suggestedMax: Math.max.apply(null, day7_list[1]) + Math.min.apply(null, day7_list[1]) * 0.05,
                grid: {
                    display : false
                },

            },
            y2: {
                beginAtZero: true,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, day7_list[2]),
                suggestedMax: Math.max.apply(null, day7_list[2])* 3,
                grid: {
                    display : false
                },
            },
        }
    }
});

// 1개월 종가 - 거래량 차트
var month1_close_LineChart = new Chart(month1_line, {
    data: {
        labels: month1_list[0],
        datasets: [{
            type: 'line',
            label: '1개월 종가',
            data: month1_list[1],
            pointStyle: 'dash',
            backgroundColor: 'rgba(253, 126, 20, 1)',
            borderColor: 'rgba(253, 126, 20, 1)',
            yAxisID : 'y',
        },{
            type: 'bar',
            label: '1개월 거래량',
            data: month1_list[2],
            backgroundColor: 'rgba(117, 183, 152, 1)',
            borderColor: 'rgba(117, 183, 152, 1)',
            barPercentage: 1,
            yAxisID : 'y2',
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: false, // 정적 동적 크기 변경?
        legend: false, //범례 표시 안함
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: { //마우스를 근처에 가져갔을 때, 데이터 값 표시
            mode: 'nearest',
            intersect: true
        },
        scales:{
            x: {
                display: false,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'left',
                suggestedMin: Math.min.apply(null, month1_list[1]) - Math.min.apply(null, month1_list[1]) * 0.1,
                suggestedMax: Math.max.apply(null, month1_list[1]) + Math.min.apply(null, month1_list[1]) * 0.05,
                grid: {
                    display : false
                },

            },
            y2: {
                beginAtZero: true,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, month1_list[2]),
                suggestedMax: Math.max.apply(null, month1_list[2])* 3,
                grid: {
                    display : false
                },
//                ticks: {
//                    stepSize: 1
//                }
            },
        }
    }
});


// 3개월 차트
var month3_LineChart = new Chart(month3_line, {
    data: {
        labels: month3_list[0],
        datasets: [{
            type: 'line',
            label: '3개월 종가',
            data: month3_list[1],
            pointStyle: 'dash',
            backgroundColor: 'rgba(253, 126, 20, 1)',
            borderColor: 'rgba(253, 126, 20, 1)',
            yAxisID : 'y',
        },{
            type: 'bar',
            label: '3개월 거래량',
            data: month3_list[2],
            backgroundColor: 'rgba(117, 183, 152, 1)',
            borderColor: 'rgba(117, 183, 152, 1)',
            barPercentage: 1,
            yAxisID : 'y2',
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: false, // 정적 동적 크기 변경?
        legend: false, //범례 표시 안함
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: { //마우스를 근처에 가져갔을 때, 데이터 값 표시
            mode: 'nearest',
            intersect: true
        },
        scales:{
            x: {
                display: false,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'left',
                suggestedMin: Math.min.apply(null, month3_list[1]) - Math.min.apply(null, month3_list[1]) * 0.1,
                suggestedMax: Math.max.apply(null, month3_list[1]) + Math.min.apply(null, month3_list[1]) * 0.05,
                grid: {
                    display : false
                },
            },
            y2: {
                beginAtZero: true,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, month3_list[2]),
                suggestedMax: Math.max.apply(null, month3_list[2])* 3,
                grid: {
                    display : false
                },
            },
        }
    }
});


//------------------------ 1년 차트
var year1_LineChart = new Chart(year1_line, {
    data: {
        labels: year1_list[0],
        datasets: [{
            type: 'line',
            label: '1년 종가',
            data: year1_list[1],
            pointStyle: 'dash',
            backgroundColor: 'rgba(253, 126, 20, 1)',
            borderColor: 'rgba(253, 126, 20, 1)',
            borderWidth : 5,  // 선 두께
            yAxisID : 'y',
        },{
            type: 'bar',
            label: '1년 거래량',
            data: year1_list[2],
            backgroundColor: 'rgba(117, 183, 152, 1)',
            borderColor: 'rgba(117, 183, 152, 1)',
            barPercentage: 0.8,
            yAxisID : 'y2',
        }]
    },
    options: {
        maintainAspectRatio: false,
        responsive: false, // 정적 동적 크기 변경?
        legend: false, //범례 표시 안함
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: { //마우스를 근처에 가져갔을 때, 데이터 값 표시
            mode: 'nearest',
            intersect: true
        },
        scales:{
            x: {
                display: false,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'left',
                suggestedMin: Math.min.apply(null, year1_list[1]) - Math.min.apply(null, year1_list[1]) * 0.5,
                suggestedMax: Math.max.apply(null, year1_list[1]) + Math.min.apply(null, year1_list[1]) * 0.2,

                grid: {
                    display : false
                },
            },
            y2: {
                beginAtZero: true,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, year1_list[2]),
                suggestedMax: Math.max.apply(null, year1_list[2])* 2,
                grid: {
                    display : false
                },
            },
        }
    }
});
