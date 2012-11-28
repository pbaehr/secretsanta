String.prototype.trim = function() { return this.replace(/^\s\s*/, '').replace(/\s\s*$/, '');};

$(document).ready(function()
{
    $('#reveal').click(function()
    {
        var personId = $("#picker").val();
        if(personId == '--')
            return;

        _this = $(this);
        _this.unbind('click');
        _this.css({'cursor': 'auto'});

        $("#tearing")[0].play();
        $.get('/pick/' + personId, function(name)
            {
                _this.find('span.name').text(name.trim());
                _this.find('p').show();
                _this.animate({'width': 500});
                _this.find('p').animate({'width': 475});
            });
    });
    $("#reveal .reset").click(function(e)
    {
        e.preventDefault();
        location.reload(true);
    });
});
