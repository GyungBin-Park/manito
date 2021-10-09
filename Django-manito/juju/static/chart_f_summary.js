// 포괄손익계산서 - 재무 상태표 차트

// 재무상태표
var f_summary_1_line = document.getElementById('f_summary_1_chart').getContext('2d');
var f_summary_2_line = document.getElementById('f_summary_2_chart').getContext('2d');


// 재무제표 차트 1
var summary1_LineChart = new Chart(f_summary_1_line, {
    data: {
//        labels: f_summary_list[0],    // date
        labels: f_summary_list[0],
        datasets: [{
            type: 'bar',
            label: '매출액(억)',
            data : f_summary_list[1],         // sale - 매출액
            backgroundColor: 'rgba(128, 189, 255, 1)',
            borderColor: 'rgba(128, 189, 255, 1)',
            barPercentage: 1,
            yAxisID : 'y',
            order : 3,
            borderRadius : 5,
        },{
            type: 'bar',
            label: '영업이익(억)',
            data: f_summary_list[2],        // profit - 영업이익
            backgroundColor: 'rgba(239, 173, 206, 1)',
            borderColor: 'rgba(239, 173, 206, 1)',
            barPercentage: 1,
            yAxisID : 'y',
            order : 4,
            borderRadius : 5,
        },{
            type: 'bar',
            label: '당기순이익(억)',
            data: f_summary_list[3],        // ni - 당기순이익
            backgroundColor: 'rgba(117, 183, 152, 1)',
            borderColor: 'rgba(117, 183, 152, 1)',
            barPercentage: 1,
            yAxisID : 'y',
            order : 5,
            borderRadius : 5,

        },{
            type: 'line',
            label: '영업이익률(%)',
            data: f_summary_list[4],        // margin_r - 영업이익률
            backgroundColor: 'rgba(173, 72, 209, 1)',
            borderColor: 'rgba(173, 72, 209, 1)',
            yAxisID : 'y2',
            radius : 5,
            order : 1,
        },{
            type: 'line',
            label: 'ROE(%)',
            data: f_summary_list[5],        // roe
            backgroundColor: 'rgba(47, 12, 147, 1)',
            borderColor: 'rgba(47, 12, 147, 1)',
            yAxisID : 'y2',
            radius : 5,
            order : 2
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
        scales: {
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
                suggestedMin: 0,
                suggestedMax: Math.max.apply(null, f_summary_list[1]) * 1.1,
                // 자산 총계 기준 ( min, max )
                grid: {
                    display : false
                },
            },
            y2: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, f_summary_list[5]) * 1.4,
                suggestedMax: Math.max.apply(null, f_summary_list[5]) * 1.4,
                grid: {
                    display : false
                },
            },
        }
    }
});



// 재무제표 차트 2
var summary2_LineChart = new Chart(f_summary_2_line, {
    data: {
        labels: f_summary_list[0],
        datasets: [{
            type: 'line',
            label: '부채 비율',
            data: f_summary_list[8],
            backgroundColor: 'rgba(77, 212, 172, 1)',
            borderColor: 'rgba(77, 212, 172, 1)',
            borderWidth : 5,  // 선 두께
            yAxisID: 'y2',
            order : 1,
            radius : 5,
        },{
            type: 'bar',
            label: '자산 총계',
            data: f_summary_list[6],
            backgroundColor: 'rgba(89, 53, 154, 1)',
            borderColor: 'rgba(89, 53, 154, 1)',
            barPercentage: 1,
            yAxisID: 'y',
            order : 2,
            borderRadius : 5,

        },{
            type: 'bar',
            label: '부채 총계',
            data: f_summary_list[7],
            backgroundColor: 'rgba(255, 193, 7, 1)',
            borderColor: 'rgba(255, 193, 7, 1)',
            barPercentage: 1,
            yAxisID: 'y',
            order : 3,
            borderRadius : 5,
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

        scales: {
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
                suggestedMin: 0,
//                suggestedMin: Math.min.apply(null, f_summary_list[6]) - Math.min.apply(null, close_list) * 0.1,
                suggestedMax: Math.max.apply(null, f_summary_list[6])
                                + Math.min.apply(null, f_summary_list[6]) * 0.05,
                // 자산 총계 기준 ( min, max )
                grid: {
                    display : false
                },
            },
            y2: {
                beginAtZero: false,
                type: 'linear',
                display: false,
                position: 'right',
                suggestedMin: Math.min.apply(null, f_summary_list[8]) - 10,
                suggestedMax: Math.max.apply(null, f_summary_list[8]) + 10,
                grid: {
                    display : false
                },
            },
        }
    }
});

