// kospi 200 chart


var kospi200_line = document.getElementById('kospi200_LineChart').getContext('2d');

var kospi200_Chart = new Chart(kospi200_line, {
//    type: 'line',
    data: {
        // labels: [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        labels: date_list,
        datasets: [{
            type: 'line',
            label: 'kospi 200',
            data: close_list,
            pointStyle: 'dash',
            backgroundColor: 'rgba(209, 86, 197, 1)',
            borderColor: 'rgba(209, 86, 197, 1)',
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
                suggestedMin: Math.min.apply(null, close_list) - Math.min.apply(null, close_list) * 0.1,
                suggestedMax: Math.max.apply(null, close_list) + Math.min.apply(null, close_list) * 0.05,
                grid: {
                    display : false
                },
            },
        }
    }
});