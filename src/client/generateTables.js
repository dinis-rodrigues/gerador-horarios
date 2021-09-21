// Table navigation
var current = 1;
var totalCombinations = 0;

var courseCount = 0;

function showTable(i) {
  document.getElementById("tt" + i).style.display = "block";
}
function hideTable(i) {
  document.getElementById("tt" + i).style.display = "none";
}
function updateLabel() {
  document.getElementById("label").innerHTML =
    current + "/" + totalCombinations;
}
function goRight() {
  hideTable(current);
  current = ((current + totalCombinations) % totalCombinations) + 1;
  showTable(current);
  updateLabel();
}
function goLeft() {
  hideTable(current);
  current = ((current + totalCombinations - 2) % totalCombinations) + 1;
  showTable(current);
  updateLabel();
}

const submitForm = () => {
  var formEl = document.forms.myForm;
  var kvpairs = [];
  var form = formEl; // get the form somehow
  for (var i = 0; i < formEl.elements.length; i++) {
    var e = form.elements[i];
    if ((e.type === "checkbox" && e.checked) || e.type !== "checkbox") {
      kvpairs.push(
        encodeURIComponent(e.name) + "=" + encodeURIComponent(e.value)
      );
    }
  }
  var queryString = kvpairs.join("&");

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      if (xmlhttp.responseText == "") console.log(error);
      else {
        document.getElementById("courseURL").value = "";
        let htmlText = xmlhttp.responseText.substring(5);

        // Get total number of combinations, this is written in the response text, just
        // find the value
        let subStringIdx =
          htmlText.indexOf("var total =") + "var total =".length;
        let subString = htmlText.substring(subStringIdx);

        let finalSubIdx = htmlText.indexOf(";") - 1;
        let finalSubString = subString.substring(0, finalSubIdx);

        totalCombinations = parseInt(finalSubString);
        current = 1;

        // console.log(htmlText());
        document.getElementById("scheduleTable").innerHTML = htmlText;
        showTable(current);
        updateLabel();
      }
    }
  };

  //   var encodedURL = encodeURIComponent(
  //     document.getElementById("courseURL").value
  //   );
  xmlhttp.open("POST", "src/api/generate_timetables.php", true);
  xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xmlhttp.send(queryString);
};

const showErrorMessage = () => {
  document.getElementById("errorMessage").style.display = "inline";
};
const hideErrorMessage = () => {
  document.getElementById("errorMessage").style.display = "none";
};

const processCourseURL = () => {
  if (courseURL.value == "") return;

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = () => {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      console.log(xmlhttp);
      if (xmlhttp.responseText == "") showErrorMessage();
      else {
        hideErrorMessage();
        document.getElementById("courseURL").value = "";
        document.getElementById("courses").innerHTML += xmlhttp.responseText;
        submitForm();
      }
    }
  };

  courseCount++;
  var encodedURL = encodeURIComponent(
    document.getElementById("courseURL").value
  );
  xmlhttp.open("POST", "src/api/process_course_url.php", true);
  xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xmlhttp.send("course_id=" + courseCount + "&url=" + encodedURL);
};

const removeCourse = (course) => {
  $("#" + course.id).remove();
  courseCount--;
  if (courseCount <= 0) {
    document.getElementById("scheduleTable").innerHTML = "";
  } else {
    submitForm();
  }
};

document.onkeyup = (event) => {
  console.log(event.key);
  const key = event.key; // "ArrowRight", "ArrowLeft", "ArrowUp", or "ArrowDown"

  if (key === "ArrowLeft") {
    goLeft();
  } else if (key === "ArrowRight") {
    goRight();
  }
};
