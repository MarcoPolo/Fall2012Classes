
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};
exports.numAnalysis = function(req, res){
  res.render('numAnalysis', { title: 'Numerical Analysis' });
};
exports.modern = function(req, res){
  res.render('modern', { title: 'Modern Physics' });
};
exports.class = function(req, res){
  res.render('index', { title: 'Express' });
};
