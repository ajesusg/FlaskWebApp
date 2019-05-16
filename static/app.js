$(document).ready(function(){
    setInterval(refresh, 40000);
        function refresh() {
        var return_first = function(){
            var tmp = null;
            $.ajax({
                url: '/datab',
                type: 'POST',
                success: function(response) {
                    tmp=response;
                    tmp = JSON.stringify(tmp);
                    vol = tmp.slice(1,3);
                    cor = tmp.slice(4,5);
                    document.getElementById("vol").innerHTML = vol;
                    document.getElementById("cor").innerHTML = cor;

                },
                
            });
            return tmp;
        }();
}
});