/**
 * Created by anaisgueyte on 13/02/2017.
 */

function deleteTask(el)
{
    if (confirm("Etes-vous sûr(e) de vouloir supprimer cette tâche ? Cette opération est irréversible !") == true)
    {
        console.log("hello");
        var id = el.id;
        console.log(id);

        var url = $(el).attr("data-url");
        console.log(url);

        $.ajax
        ({
            type: "POST",
            url: url,
            data: {
            "id": id
            },
            success: function (taskid)
            {

                $('#' + id).closest("tr").remove();


            },
            error: function (data)
            {
                console.log(data);
            }
         });
     }
}