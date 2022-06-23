const frameModal = document.querySelector('.frame')

const  openModal = document.querySelector('.add-frame')
openModal.addEventListener('click', toggleModal)

const closeModal = document.querySelectorAll('.close-modal')
closeModal[0].addEventListener('click', toggleModal)
closeModal[1].addEventListener('click', toggleTaskModal)
function toggleModal(){
    frameModal.classList.toggle('active')
}
const taskModal = document.querySelector('.task')

const taskButtons = document.querySelectorAll('.add-task')
taskButtons.forEach((item) =>{
    item.addEventListener('click', toggleTaskModal)
})
function toggleTaskModal(){
    const frameID = this.dataset.id
    taskModal.classList.toggle('active')
    document.querySelector('#id_frame').value = frameID
}