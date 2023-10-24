function iniciarMap(){
    var coord = {lat:-33.42006549266818, lng:-70.60375023717043};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom : 15,
        center : coord
    });

    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}