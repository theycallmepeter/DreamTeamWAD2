$(function () {
	// $('#likeq').click(function(){
	$(document).on('click','#likeq', function(){
		var questionslug;
		var like;
		questionslug = $(this).attr("data-questionslug");
		like = $(this).attr("data-like")
		$.get('/gliocas_app/likequestion/', {question_slug: questionslug, like: like}, function(data){
			$('#like_count').html(data);
			//put code to change style of likebutton here
		});
	});
});

