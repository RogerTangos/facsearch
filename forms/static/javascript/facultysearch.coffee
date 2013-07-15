# You are working on making multiple fields show when you need to create an event.
# xml feed: https://www.google.com/calendar/feeds/62a1fsr3u1enj5h3ij02grkdqs%40group.calendar.google.com/public/basic
# to get calendar data: $('#calendar').fullCalendar( 'clientEvents')

event_data = {{event_data}}

selectedEvent = null
selectedStart = null
selectedEnd = null
selectedAllDay = null

saveEvent = () ->
  title = $('#title').val()
  location = $('#location').val()
  phone = $('#phone').val()
  detail = $('#detail').val()

  # behavior changes depending on whether event is new or not
  if selectedEvent != null
    selectedEvent.title = title
    selectedEvent.location = location
    selectedEvent.phone = phone
    selectedEvent.detail = detail
    $('#calendar').fullCalendar('updateEvent', selectedEvent)
    console.log 'event updated'
  else
    selectedEvent = {}
    selectedEvent.title = title
    selectedEvent.start = selectedStart
    selectedEvent.end = selectedEnd
    selectedEvent.allDay = selectedAllDay
    selectedEvent.location = location
    selectedEvent.phone = phone
    selectedEvent.detail = detail

    $('#calendar').fullCalendar('addEventSource', [selectedEvent]) 
    console.log 'event added'

  $('.closeBtn').click()

deleteEvent = () ->
  $('#calendar').fullCalendar("removeEvents", selectedEvent._id)
  $('.closeBtn').click()

$(document).ready ->
      # $('#calendar').fullCalendar({events: 'https://www.google.com/calendar/feeds/62a1fsr3u1enj5h3ij02grkdqs%40group.calendar.google.com/public/basic'})

 
 # this section is no longer necessary. need to clean up 2013-06-24 arc
  # initialize the external events
  #   -----------------------------------------------------------------
  $("#external-events div.external-event").each ->
    
    # create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
    # it doesn't need to have a start or end
    eventObject = title: $.trim($(this).text()) # use the element's text as the event title
    
    # store the Event Object in the DOM element so we can get to it later
    $(this).data "eventObject", eventObject
    
    # make the event draggable using jQuery UI
    $(this).draggable
      zIndex: 999
      revert: true # will cause the event to go back to its
      revertDuration: 0 #  original position after the drag


  
  # initialize the calendar
  #   -----------------------------------------------------------------
  $("#calendar").fullCalendar
    header:
      left: "prev,next today"
      center: "title"
      right: "month,agendaWeek,agendaDay"

    selectable: true
    editable: true

    select: (start, end, allDay) ->
      $('.modalLink').click()
      selectedEvent = null
      selectedStart = start
      selectedEnd = end
      selectedAllDay = allDay

    eventClick: (calEvent, jsEvent, view) ->
      selectedEvent = calEvent
      $('#title').val(calEvent.title)
      $('#location').val(calEvent.location)
      $('#phone').val(calEvent.phone)
      $('#detail').val(calEvent.detail)
      
      $('.modalLink').click()

      # Add db events
      # $("#calendar").fullCalendar('addEventSource', event_data)
    
# modal window
`$('.modalLink').modal({
  trigger: '.modalLink',
  olay: 'div.overlay',
  modals: 'div.modal',
  animationEffect: 'slidedown',
  animationSpeed: 400,
  moveModalSpeed: 'slow',
  background: '00c2ff',
  opacity: 0.8,
  openOnLoad: false,
  docClose: true,
  closeByEscape: true,
  moveOnScroll: true,
  resizeWindow: true,
  video: 'http://player.vimeo.com/video/9641036?color=eb5a3d',
  close: '.closeBtn'
});`

