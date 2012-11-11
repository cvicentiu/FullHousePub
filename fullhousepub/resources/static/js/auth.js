function doLogin ()
{
	document.Login.submit() ;
};
$(document).ready(function () {

	var makeAllFormSubmitOnEnter = function () {
		$('form input, form select').live('keypress', function (e) {
			if (e.which && e.which == 13) {
				$(this).parents('form').submit();
				return false;
			}
			else
		{
			return true;
		}
		});
	};
	makeAllFormSubmitOnEnter();
});

