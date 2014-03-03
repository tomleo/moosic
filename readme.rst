Moosic
======

Moosic is a media player that makes it easy to keep track of music you like.
Spotify is great but sometimes you can't find an album you like, or a live recording/bootleg. A lot
of times you can only find songs on youtube, but sometimes those songs get taken down due to
copywrite infringment.

The idea of moosic is to store as much meta data about a song, and if a file is available attempt
to sync  the "cloud" metadata with the file metadata (IDv3 tag). Also moosic contains collections
of song objects that contain various sources for the media itself. So for example you can specify
songs with metadata in your library that you do not own, or you can add songs and stream them from
spotify or youtube via a moosic client.

Will eventually look into scrobbling things with Last.fm.

The Stack
---------

The backend is Django with Django Rest Framework, and is responsible to persisting and searching
for data.

 - django 1.6
 - django_rest
 - south
 - postgresql
 - (maybe elasticsearch?)
 - (nose)

The front end is HTML5/CSS/JS.

 - google polymer
 - backbone.js
 - (find test framework)
 - npm, grunt, bower, yeoman, jshint
 - (jquery or underscorejs) http://underscorejs.org/
 - RequireJS
 - Crossroads.js http://millermedeiros.github.io/crossroads.js/
 - Hasher https://github.com/millermedeiros/hasher/
 - Jasmine http://jasmine.github.io/2.0/introduction.html
