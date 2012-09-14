
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , http = require('http')
  , path = require('path')
  , fs = require('fs')
  , marked = require('marked');


// Set default options
marked.setOptions({
  gfm: true,
  pedantic: false,
  sanitize: false,
  // callback for code highlighter
  highlight: function(code, lang) {
    if (lang === 'js') {
      return javascriptHighlighter(code);
    }
    return code;
  }
});

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  //app.set('view engine', 'jade');
  //app.set('view engine', 'markdown');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(path.join(__dirname, 'public')));

  app.engine('md', function(path, options, fn){
    fs.readFile(path, 'utf8', function(err, str){
      if (err) return fn(err);
      str = marked(str);
      fn(null, str);
    });
  });

});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
app.get('/class',routes.class);

app.get('/numAnalysis',routes.numAnalysis);
app.get('/numAnalysis/:id', routes.numAnalysisPage)

app.get('/modern',routes.modern);




http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
