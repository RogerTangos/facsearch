(function() {
  var deleteEvent, saveEvent, selectedAllDay, selectedEnd, selectedEvent, selectedStart, sendToServer;

  deleteEvent = void 0;

  saveEvent = void 0;

  selectedAllDay = void 0;

  selectedEnd = void 0;

  selectedEvent = void 0;

  selectedStart = void 0;

  selectedEvent = null;

  selectedStart = null;

  selectedEnd = null;

  selectedAllDay = null;

  
function cloneEvent(obj) {
  var copy = {};
  var fields = ['title', 'start', 'end', 'allDay', 'location', 'phone', 'detail', 'status'];
  var field;
  for (var ind in fields) {
    field = fields[ind];
    if (field in obj) {
      copy[field] = obj[field];
    }
  }
  return copy;
}
;

  window.saveEvent = function() {
    var detail, location, phone, title;
    detail = void 0;
    location = void 0;
    phone = void 0;
    title = void 0;
    title = $("#title").val();
    location = $("#location").val();
    phone = $("#phone").val();
    detail = $("#detail").val();
    if (selectedEvent === null) {
      selectedEvent = {};
      selectedEvent.title = title;
      selectedEvent.start = selectedStart;
      selectedEvent.end = selectedEnd;
      selectedEvent.allDay = selectedAllDay;
      selectedEvent.location = location;
      selectedEvent.phone = phone;
      selectedEvent.detail = detail;
      selectedEvent.status = 'new';
      $("#calendar").fullCalendar("addEventSource", [selectedEvent]);
      console.log("event added localllly");
      sendToServer('new', cloneEvent(selectedEvent));
    } else {
      selectedEvent.title = title;
      selectedEvent.location = location;
      selectedEvent.phone = phone;
      selectedEvent.detail = detail;
      selectedEvent.status = 'edit';
      $("#calendar").fullCalendar("updateEvent", selectedEvent);
      sendToServer('edit', cloneEvent(selectedEvent));
      $(".closeBtn").click();
    }
    return false;
  };

  deleteEvent = function() {
    $("#calendar").fullCalendar("removeEvents", selectedEvent._id);
    sendToServer('delete', selectedEent);
    $(".closeBtn").click();
    return false;
  };

  sendToServer = function(action, data) {
    console.log('foo');
    $.ajax({
      data: data,
      type: $("#submit_event").attr("method"),
      url: "/forms/visitor/1/event",
      success: function(response) {
        return false;
      }
    });
    return false;
  };

  $(document).ready(function() {
    $("#external-events div.external-event").each(function() {
      var eventObject;
      eventObject = void 0;
      eventObject = {
        title: $.trim($(this).text())
      };
      $(this).data("eventObject", eventObject);
      return $(this).draggable({
        zIndex: 999,
        revert: true,
        revertDuration: 0
      });
    });
    return $("#calendar").fullCalendar({
      header: {
        left: "prev,next today",
        center: "title",
        right: "month,agendaWeek,agendaDay"
      },
      selectable: true,
      editable: true,
      select: function(start, end, allDay) {
        $(".modalLink").click();
        selectedEvent = null;
        selectedStart = start;
        selectedEnd = end;
        return selectedAllDay = allDay;
      },
      eventClick: function(calEvent, jsEvent, view) {
        selectedEvent = calEvent;
        $("#title").val(calEvent.title);
        $("#location").val(calEvent.location);
        $("#phone").val(calEvent.phone);
        $("#detail").val(calEvent.detail);
        return $(".modalLink").click();
      }
    });
  });

  $(".modalLink").modal({
    trigger: ".modalLink",
    olay: "div.overlay",
    modals: "div.modal",
    animationEffect: "slidedown",
    animationSpeed: 400,
    moveModalSpeed: "slow",
    background: "00c2ff",
    opacity: 0.8,
    openOnLoad: false,
    docClose: true,
    closeByEscape: true,
    moveOnScroll: true,
    resizeWindow: true,
    video: "http://player.vimeo.com/video/9641036?color=eb5a3d",
    close: ".closeBtn"
  });

}).call(this);
