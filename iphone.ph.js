var system = require('system');
var args = system.args;
var webPage = require('webpage');
var page = webPage.create();

if (args.length != 2) {
	phantom.exit()
}

page.settings.userAgent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7';

page.viewportSize = { width: 320, height: 480 };
page.open(args[1], function start(status) {
	page.evaluate(function() {
		if (!document.body.bgColor) document.body.bgColor = 'white';
	});

	setTimeout(function(){
		page.render('mobile.png');
		phantom.exit();
	}, 1000);
});
