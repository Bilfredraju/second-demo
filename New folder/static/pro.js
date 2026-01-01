function getprodata() {
      var xhttp = new XMLHttpRequest();
      xhttp.open(
        "GET",
        "/product/getpro/" + document.getElementById("keyword").value,
        true
      );
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
          var data = JSON.parse(this.responseText)
          console.log(data.produ)
          str = "<table>";
            for (x of data.produ) {
              str = str + "<tr>"
              str = str + "<td>" + x.name + "</td>"
            }
          str = str + "</table>"
          document.getElementById("data").innerHTML = str
        }
      };
      xhttp.send();
    }
function drawalldata(){
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET','/product/jdata/', true)
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var data = JSON.parse(this.responseText)
            console.log(data.new)
        }
    };
    xhttp.send();
}
    
function drawdata(){
    const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
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