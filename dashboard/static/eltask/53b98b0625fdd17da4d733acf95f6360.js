var hivetheme={getSelector:function(a){return"[data-component=\""+a+"\"]"},getComponent:function(a){return jQuery(this.getSelector(a))}};(function(a){"use strict";a(document).ready(function(){hivetheme.getComponent("menu").each(function(){var b=a(this).children("ul");a(this).find("li").each(function(){var b=a(this);b.children("ul").length&&(b.addClass("parent"),b.hoverIntent(function(){if(b.parent("ul").parent("li").hasClass("parent")){var c=b.parent(),d=c.offset().left+2*c.outerWidth();b.children("ul").removeClass("left").removeClass("right"),d>a(window).width()?b.children("ul").addClass("left").css("left",-c.outerWidth()):b.children("ul").addClass("right")}b.addClass("active"),b.children("ul").slideDown(150)},function(){b.children("ul").slideUp(150,function(){b.removeClass("active")})})),b.children("a").on("click",function(b){"#"===a(this).attr("href")&&b.preventDefault()})}),b.children("li").each(function(){if(a(this).offset().top>b.offset().top)return b.addClass("wrap"),!1})}),hivetheme.getComponent("burger").each(function(){var b=a(this).children("ul");b.css("top",a("#wpadminbar").height()),a(this).children("a").on("click",function(c){a("body").css("overflow-y","hidden"),b.fadeIn(150),c.preventDefault()}),b.on("click",function(c){a(c.target).is("a")||a(c.target).is("li.parent")||(a("body").css("overflow-y","auto"),b.fadeOut(150))}),b.find("li").each(function(){var b=a(this);b.children("ul").length&&(b.addClass("parent"),b.on("click",function(c){a(c.target).is(b)&&(b.toggleClass("active"),b.children("ul").slideToggle(150))})),b.children("a").on("click",function(b){"#"===a(this).attr("href")&&b.preventDefault()})})})}),a("body").imagesLoaded(function(){hivetheme.getComponent("loader").fadeOut()})})(jQuery)
;