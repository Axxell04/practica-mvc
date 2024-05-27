const sectionTareas = document.getElementById("section-tareas");

const templateMiembro = document.getElementById("template-miembro").content;
const templateTarea = document.getElementById("template-tarea").content;

const containerMiembros = document.getElementById("container-miembros");
const containerTareas = document.getElementById("container-tareas");

const btnAddMiembro = document.getElementById("btn-add-miembro");
const inputNombre = document.getElementById("input-nombre");
const btnAddTarea = document.getElementById("btn-add-tarea");
const inputDescripcion = document.getElementById("input-descripcion");
const miembroSelectName = document.getElementById("miembro-select-name");

const URLServer = window.location.origin;
let idMiembroSelected = 0;

document.addEventListener("DOMContentLoaded", () => {
    getMiembros();
    if (idMiembroSelected === 0) {
        sectionTareas.style.opacity = 0;
    }
});

btnAddMiembro.addEventListener("click", (e) => {
    if (inputNombre.value !== "") {
        addMiembro(inputNombre.value);
        inputNombre.value = "";
    }
})

btnAddTarea.addEventListener("click", (e) => {
    if (inputDescripcion.value !== "") {
        addTarea(inputDescripcion.value);
        inputDescripcion.value = "";
    }
})

const pintarMiembros = (miembros) => {
    containerMiembros.innerHTML = "";
    miembros.map((miembro) => {
        const template = templateMiembro.cloneNode(true);
        const cardMiembro = template.querySelector(".card-miembro");
        const btnName = template.querySelector(".btn-nombre");
        const btnDelete = template.querySelector('.btn-eliminar');

        cardMiembro.dataset.id_miembro = miembro.id_miembro;
        btnName.textContent = miembro.nombre;
        // console.log(cardMiembro)

        btnName.addEventListener("click", (e) => {
            idMiembroSelected = e.target.parentElement.dataset.id_miembro;
            miembroSelectName.textContent = e.target.textContent;
            getTareas(idMiembroSelected);
            sectionTareas.style.opacity = 1;
        });

        btnDelete.addEventListener("click", (e) => {
            const id_miembro = e.target.parentElement.dataset.id_miembro;
            deleteMiembro(id_miembro);
        })

        containerMiembros.appendChild(template);
    })
}

const pintarTareas = (tareas) => {
    containerTareas.innerHTML = "";
    tareas.map((tarea) => {
        const template = templateTarea.cloneNode(true);
        const cardTarea = template.querySelector(".card-tarea");
        const descripcion = template.querySelector(".descripcion");
        const btnEliminar = template.querySelector(".btn-eliminar");

        cardTarea.dataset.id_tarea = tarea.id_tarea;
        descripcion.textContent = tarea.descripcion;

        btnEliminar.addEventListener("click", (e) => {
            const id_tarea = e.target.parentElement.dataset.id_tarea;
            deleteTarea(id_tarea);
        })

        containerTareas.appendChild(template);
    })
}

const addMiembro = async (nombre) => {
    const res = await fetch(`${URLServer}/add_miembro`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre: nombre
        })
    });
    if (res.ok) {
        getMiembros();
    }
}

const getMiembros = async () => {
    const res = await fetch(`${URLServer}/get_miembros`);
    const data = await res.json()
    console.log(data)
    if (data) {
        pintarMiembros(data);
    }
}

const deleteMiembro = async (id_miembro) => {
    const res = await fetch(`${URLServer}/remove_miembro`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id_miembro: id_miembro
        })
    })

    if (res.ok) {
        // window.location.reload();
        getMiembros();
        sectionTareas.style.opacity = 0;
    }
}

const addTarea = async (descripcion) => {
    const res = await fetch(`${URLServer}/add_tarea`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id_miembro: idMiembroSelected,
            descripcion: descripcion
        })
    });
    if (res.ok) {
        getTareas();
    }
}

const getTareas = async () => {
    const res = await fetch(`${URLServer}/get_tareas/${idMiembroSelected}`)
    const data = await res.json()
    if (data) {
        console.log(data)
        pintarTareas(data);
    }
}

const deleteTarea = async (id_tarea) => {
    const res = await fetch(`${URLServer}/remove_tarea`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id_tarea: id_tarea
        })
    })

    if (res.ok) {
        getTareas();
    }

}
