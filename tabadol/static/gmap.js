// Initialize and add the map
      function initMap() {
        // The location of Berlin
      const berlin = { lat: 52.5200, lng: 13.4050};
        // The map, centered at Berlin
         const map = new google.maps.Map(document.getElementById("map"), {
         zoom: 11,
         center: berlin,
        });
        // The marker, positioned at Berlin
       const marker = new google.maps.Marker({
          position: berlin,
          map: map,
        });
     }



// Initialize and add the map without marker

/*let map;

function initMap() {
  console.log('InitMap')
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 52.5200, lng: 13.4050 },
    zoom: 10,
  });
}*/
