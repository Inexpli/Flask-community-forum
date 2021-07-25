function editButton() {
    console.log('działam')
};

function showEdit(noteId) {
  var title = document.getElementById('titleEdit')
  var titleContent = document.getElementById(`noteTitleValue${noteId}`).innerText
  var note = document.getElementById('noteEdit')
  var noteContent = document.getElementById(`noteValue${noteId}`).innerText
  title.value = titleContent
  note.value = noteContent
  document.getElementById('submitEdit').setAttribute('onClick',`editNote(${noteId})`)
}

function editNote(noteId) {
  var titleContent = document.getElementById('titleEdit').value
  var noteContent = document.getElementById('noteEdit').value
  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId, title: titleContent, note: noteContent }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function showDelete(noteId) {
  document.getElementById('deleteShow').setAttribute('onClick',`deleteNote(${noteId})`)
}

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
