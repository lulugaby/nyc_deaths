public class jconnect{


    $.ajax({
    url: "https://data.cityofnewyork.us/resource/jb7j-dtam.json",
    type: "GET",
    data: {
      "$limit" : 5000,
      "$$app_token" : "J5F17tXpdVYQUtsJEjvqXn9Li"}
}).done(function(data) {
  alert("Retrieved " + data.length + " records from the dataset!");
  console.log(data);
});
document.write("done");


public static void main(String[] args){

}

}