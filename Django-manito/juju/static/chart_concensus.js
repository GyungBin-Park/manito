// 컨센서스 차트
var concensus_line = document.getElementById('concensus_chart').getContext('2d');

var myMax = Math.ceil(Math.floor((Math.max.apply(null, concensus_target_prc) + Math.max.apply(null, concensus_target_prc)/10)) / 1000) * 1000;
var myMin = Math.ceil(Math.floor((Math.min.apply(null, concensus_target_prc) - Math.min.apply(null, concensus_target_prc)/10)) / 1000) * 1000;

////////////////////////////////////////////////////////
// ---------------- 컨센서스 라인 차트
var concensus_Chart = new Chart(concensus_line, {
    data: {
        labels: concensus_date,
        datasets: [{
            type: 'line',
            label: '목표 주가',
            data: concensus_target_prc,
            backgroundColor: 'rgba(113, 164, 239, 1)',
            borderColor: 'rgba(113, 164, 239, 1)',
            borderWidth : 5,  // 선 두께
            yAxisID: 'y',

        },{
            type: 'line',
            label: '현재 주가',
            data: concensus_close,
            backgroundColor: 'rgba(77, 212, 172, 1)',
            borderColor: 'rgba(77, 212, 172, 1)',
            borderWidth : 5,  // 선 두께
            yAxisID: 'y',
        },
        {
            type: 'bar',
            label: '추천 점수',
            data: concensus_recom_cd,
            backgroundColor: 'rgba(234, 134, 143, 1)',
            borderColor: 'rgba(234, 134, 143, 1)',
            order : 2,
            barPercentage: 0.5,
            borderRadius : 10,
            yAxisID: 'y2',

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
        interaction: {
            mode: 'index',
            intersect: false,
        },
        scales: {
            x: {
                display: true,
                position: 'bottom',
                grid: {
                    display : false
//                    stepSize: 20,
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: true,
                position: 'right',
                suggestedMax: myMax,
                suggestedMin: myMin,
                grid: {
                    display : false
//                    stepSize: 20,
                },
                ticks: {
                    stepSize: (myMax + myMin)/2

                }
            },
            y2: {
                beginAtZero: true,
                type: 'linear',
                display: true,
                position: 'left',
                suggestedMin: 0,
                suggestedMax: 5,
                 grid: {
                    display : false
//                    stepSize: 20,
                },
                ticks: {
                    stepSize: 1
                }
//                // grid line settings
//                grid: {
//                    drawOnChartArea: false, // only want the grid lines for one axis to show up
//                },
            },
        }
    }
});
