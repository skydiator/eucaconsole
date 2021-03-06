/**
 * Copyright 2017 Ent. Services Development Corporation LP
 *
 * @fileOverview Notification pagek for client side events
 * @requires jQuery
 *
 */
var Notify = (function() {
    var _displayNotification = function (message, type) {
        $("#notifications").append($('<div class="marked">').append(
            $('<div class="alert-box">')
                .addClass(type)
                .append($('<div class="icon">')
                    .append($('<span>')))
                .append($('<div class="message">')
                    .text(message))
                .append($('<a class="close">&times;</a>')
                    .click(function () {
                        Notify.clear();
                    }))));
    };

    return {
        success: function(message) {
            _displayNotification(message, 'success');
            setTimeout(function(){
                Notify.clear();
            }, 5000);
        },
        failure: function(message) {
            _displayNotification(message, 'alert');
        },
        warn: function (message) {
            _displayNotification(message, 'warning');
        },
        info: function (message) {
            _displayNotification(message, 'info');
        },
        clear: function() {
            $("#notifications").text("");
        }
    };
}());
