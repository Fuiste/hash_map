$(function(){

  var A = App;
  var m = DS.Model;
  var a = DS.attr;

  A.User = m.extend({
    email: a('string')
  });

});
