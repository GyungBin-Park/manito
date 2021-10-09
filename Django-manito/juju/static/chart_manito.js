// 컨센서스 차트
var manito_line = document.getElementById('manito_Chart').getContext('2d');

////////////////////////////////////////////////////////
// ---------------- 컨센서스 라인 차트
var concensus_Chart = new Chart(manito_line, {
    data: {
        labels: manito_list[0],
        datasets: [{
            type: 'line',
            label: '실제 종가',
            data: manito_list[1],
            backgroundColor: 'rgba(156, 174, 199, 1)',
            borderColor: 'rgba(156, 174, 199, 1)',
            borderWidth : 2,  // 선 두께
            pointStyle: 'star',
            radius : 2,
            yAxisID: 'y',

        },{
            type: 'line',
            label: '예측 종가',
            data: manito_list[2],
            backgroundColor: 'rgba(102, 16, 242, 1)',
            borderColor: 'rgba(102, 16, 242, 1)',
            borderWidth : 5,  // 선 두께
            pointStyle: 'rectRot',
            radius : 2,
            yAxisID: 'y',
        }
        ]
    },
    options: {
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    font: {
                        size: 12,
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
                display: false,
                position: 'bottom',
                grid: {
                    display : false
                }
            },
            y: {
                beginAtZero: false,
                type: 'linear',
                display: true,
                position: 'left',
                suggestedMax: manito_list[3],
                suggestedMin: manito_list[4],
                grid: {
                    display : false
//                    stepSize: 20,
                }
            }
        }
    }
});
