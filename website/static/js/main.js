function editButton() {
    console.log('działam')
};

// // function deleteNote(noteId) {
// //     fetch("/delete-note", {
// //       method: "POST",
// //       body: JSON.stringify({ noteId: noteId }),
// //     }).then((_res) => {
// //       window.location.href = "/";
// //     });
// // }

function showEdit(noteId, noteTitle, noteContent) {
  var title = document.getElementById('titleEdit')
  var note = document.getElementById('noteEdit')
  title.value = `${noteTitle}`
  note.value = `${noteContent}`
  document.getElementById('submitEdit').setAttribute('onClick',`editNote(${noteId})`)
}

// function editNote(noteId) {
//   fetch("/edit-note", {
//     method: "POST",
//     // body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   });
// }


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



// function editButton() {
//     console.log('Stage 1')
//     var button = document.getElementById('submitEdit')
//     var titleEdit = document.getElementById('titleEdit')
//     // var titleEditValue = target.closest('noteTitleValue').innerText
//     var titleEditValue = document.getElementById('noteTitleValue').innerText
//     var noteEdit = document.getElementById('noteEdit')
//     var noteEditValue = document.getElementById('noteValue').innerText
//     titleEdit.value = titleEditValue
//     noteEdit.value = noteEditValue
// }
