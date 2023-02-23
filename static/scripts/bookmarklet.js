(function(){
    var jquery_version = '3.4.1';
    var site_url ='https://127.0.0.1:8000/';
    var static_url = site_url + 'static/'
    var min_width = 100
    var min_height  = 100


    function bookmarklet(msg){
        var css = jQuery('<link>')
        css.atr({'rel':'stylesheet',
                   'type':'text/css',
                    'href': static_url +'styles.css?r=' +
                     Math.floor(Math.random()*99999999999999999999)})
                     jQuery('head').append(css)
box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
                       jQuery('body').append(box_html);
                       // close event
                       jQuery('#bookmarklet #close').click(function(){
                          jQuery('#bookmarklet').remove();
                       });
                  };

    if (typeof window.jQuery !== 'undefined'){
        bookmarklet();
    }
    else{
        var conflicts = typeof window.$ != 'undefined'
        var script = document.createElement('script')
        script.src  = '//ajax.googleapis.com/ajax/libs/jquery/' +
        jquery_version + '/jquery.min.js';
        document.head.appendChild(script)


        var attempts  = 15;

        (function(){
            if (typeof window.jQuery == 'undefined'){
                if (--attempts > 0){
                    window.setTimeout(arguments.callee,250)
                }
                else{
                    alert('an error occurred while calling jquery')
                }
            }
            else{
                bookmarklet();
            }
        })()
    }
})()