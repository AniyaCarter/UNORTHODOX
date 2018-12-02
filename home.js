// <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js">
// function subscriptionPopup(){
//     // get the mPopup
//     var mpopup = $('#mpopupBox');
//
//     // open the mPopup
//     mpopup.show();
//
//     // close the mPopup once close element is clicked
//     $(".close").on('click',function(){
//         mpopup.hide();
//     });
//
//     // close the mPopup when user clicks outside of the box
//     $(window).on('click', function(e) {
//         if(e.target == mpopup[0]){
//             mpopup.hide();
//         }
//     });
// }
// </script>
//
// <script src="jquery.cookie.js">
// $(document).ready(function() {
//     var popDisplayed = $.cookie('popDisplayed');
//     if(popDisplayed == '1'){
//         return false;
//     }else{
//         setTimeout( function() {
//             subscriptionPopup();
//         },10000);
//         $.cookie('popDisplayed', '1', { expires: 7 });
//     }
// });
// </script>
