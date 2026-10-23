const tareas_c = document.querySelectorAll('#tarea');

const tareas_sc = document.querySelectorAll('#tarea2');

tareas_c.forEach(tarea_c => {
    tarea_c.addEventListener('dragstart', (e)  => {
    console.log("Drag started");
});

tarea_c.addEventListener('dragend', (e)  => {
    console.log("Drag ended");
});

tarea_c.addEventListener('drag', (e)  => {
    console.log("Drag in progress");
});
})


tareas_sc.forEach(tarea_sc => {
    tarea_sc.addEventListener('dragstart', (e)  => {
        console.log("Drag started");
    });

    tarea_sc.addEventListener('dragend', (e)  => {
        console.log("Drag ended");
    });

    tarea_sc.addEventListener('drag', (e)  => {
        console.log("Drag in progress");
    });
});
