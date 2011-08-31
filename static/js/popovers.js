
$.fn.ezpz_tooltip.positions.leftStatic = function(contentInfo, mouseX, mouseY, offset, targetInfo) {
    contentInfo['top'] = targetInfo['top'] - offset;
    contentInfo['left'] = targetInfo['left'] - contentInfo['width'] - offset;
	return contentInfo;
};

$(document).ready(function(){
    $(".tooltip-target").ezpz_tooltip({
        contentPosition: 'leftStatic',
        showContent: function(content) {
	      content.fadeIn('slow');
        },
	    hideContent: function(content) {
		   // if the showing animation is still running, be sure to stop it
		   // and clear the animation queue. otherwise, repeatedly hovering will
		   // cause the content to blink.
		  content.stop(true, true).fadeOut('slow');
	    }
    });
    
});
