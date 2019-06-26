const changeIndicator = (el) => {
    el.classList.toggle('has-indicator');
    console.log($(el).attr('data-pk'));
    pk = $(el).attr('data-pk');
    name = $(el).attr('name');
    value = $(el).attr('value');
    $.ajax({
        url: "/activities/schedule/button",
        type: "get", // or "get"
        data: {
            pk:pk,
            name:name,
            value:value
        }
    });
    // Provavelmente precisa fazer uma requisição AJAX pra mudar no back o
    // indicador tb
}
;