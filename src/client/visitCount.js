// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
  apiKey: "AIzaSyAHPrWvVr1El3NkJd3C0gbZbiTl_weCTlE",
  authDomain: "tsb-aplication.firebaseapp.com",
  databaseURL: "https://tsb-aplication.firebaseio.com",
  projectId: "tsb-aplication",
  storageBucket: "tsb-aplication.appspot.com",
  messagingSenderId: "124968779478",
  appId: "1:124968779478:web:0a2c6266560c594a779377",
  measurementId: "G-0Z77DRSCH6",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize Database
var db = firebase.database();

// Retrieve visit count on every page entry/refresh
db.ref("/public/scheduleWebsite/visitCount")
  .once("value")
  .then((snapshot) => {
    const visitors = snapshot.val() + 1;
    // visual count up on index.html DOM
    let demo = new countUp.CountUp("visits", visitors);
    if (!demo.error) {
      demo.start();
    } else {
      console.error(demo.error);
    }
    // Update new count on database
    db.ref("/public/scheduleWebsite/visitCount").set(visitors);
  });

// Retrieve github repo stars
fetch(`https://api.github.com/repos/dinis-rodrigues/gerador-horarios`).then(
  async (response) => {
    const data = await response.json();
    console.log(data);
    const starCount = data.stargazers_count;

    $("#starCount").text(starCount);
  }
);
