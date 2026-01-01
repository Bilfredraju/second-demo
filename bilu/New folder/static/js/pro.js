function getprodata() {
  var xhttp = new XMLHttpRequest();
  xhttp.open('GET', '/product/getproduct/' + document.getElementById('keyword').value, true)
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var data = JSON.parse(this.responseText)
      console.log(data.produ)
      str = '<table>'
      for (x of data.produ) {
        str = str + '<tr>'
        str = str + '<td>' + (x.name) + '<td>'
      }
      str = str + '</table>'
      document.getElementById('data').innerHTML = str
    }
  };
  xhttp.send();
}

function drawalldata() {
  var xhttp = new XMLHttpRequest()
  xhttp.open('GET', '/product/getalldata/', true)
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var datax = JSON.parse(this.responseText)
      console.log(datax.new)
      drawdata(datax)
    }
  };
  xhttp.send();
}

function drawdata(datax) {
  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: getlabels(datax),
      datasets: [{
        label: '# of Votes',
        data: getvalues(datax),
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

function getlabels(datax) {
  let label = []
  for (x of datax.new) {
    label.push(x.name)
  }
  return label
}

function getvalues(datax) {
  let label = []
  for (x of datax.new) {
    label.push(x.price)
  }
  return label
}