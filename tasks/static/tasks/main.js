function getAllTasks() {
    jQuery.ajax({
        url: 'tasks/load_all/',
        type: 'GET',
        dataType: "json",
        success: function(json) {
            const taskList = $("#tasksList");
            taskList.empty();
            (json.tasks).forEach(function (task) {
                console.log(task)
                const taskHTML =`
                    <tr>
                        <td>${task.title}</td>
                        <td>${task.cost} تومان</td>
                        <td>${task.time_period} روز</td>
                        <td>${task.owner}</td>
                        <td>
                            <a href=tasks/${task.id} class="btn btn-default">مشاهده کار</a>
                        </td>
                        <td>${task.state}</td>
                    </tr>`;
                taskList.append(taskHTML);
            });
        },
    });
};

console.log("connected")
$(document).ready(function() {
    $("#home").addClass("active");
    $("#allTasksButton").click(function (e) {
        console.log("clicked");
        e.preventDefault();
        getAllTasks();
    });
});