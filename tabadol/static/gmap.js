

let map;
let marker;
// Initialize and add the map
    function initMap() {
        // The location of Berlin
    const berlin = { lat: 52.5200, lng: 13.4050};
        // The map, centered at Berlin
         const map = new google.maps.Map(document.getElementById("map"), {
         zoom: 11,
         center: berlin,
             // disabling some controls. Reference: https://developers.google.com/maps/documentation/javascript/controls
         streetViewControl: false,
         fullscreenControl: true,
         mapTypeControl: false,
         mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        // The marker, positioned at Berlin
        const marker = new google.maps.Marker({
          position: berlin,
          map: map,
        });

        var mapStyles = [
          {
              "featureType": "administrative",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "road",
              "elementType": "labels",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "road",
              "elementType": "geometry.stroke",
              "stylers": [ { "visibility": "on" } ]
          },{
              "featureType": "transit",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.attraction",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.business",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.government",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.medical",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.park",
              "elementType": "labels",
              "stylers": [ { "visibility": "on" } ]
          },{
              "featureType": "poi.place_of_worship",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.school",
              "stylers": [ { "visibility": "off" } ]
          },{
              "featureType": "poi.sports_complex",
              "stylers": [ { "visibility": "on" },
               { "color": "#c9e7c9" } ]
          },{
            "featureType": "road",
            "elementType": "geometry.fill",
            "stylers": [
                { "visibility": "on" },
                { "color": "#ffffff" }
            ]
          },{
              "featureType": "landscape.man_made",
              "stylers": [
                  { "visibility": "on" },
                  { "color": "#dbdbdb" }
              ]
          },{
              "featureType": "landscape.natural",
              "elementType": "labels",
              "stylers": [ { "visibility": "off" } ]
          }
        ];
        map.setOptions({ styles: mapStyles });

  }
