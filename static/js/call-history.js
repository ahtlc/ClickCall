$(document).ready(function () {
    let pk;
    let flag = -1;
    let currentPk;
    $(".table-row").click(function (e) {
      if (pk === e.currentTarget.getAttribute(`data-pk`) || !pk || flag === -1) {
        if (!$(e.target).hasClass('icon-call-2') && !$(e.target).hasClass('icon-pay-2') && !$(e.target).hasClass('icon-email-2')) {
          $(".container-detail").slideToggle("slow");
          $(".container-detail").css("display", "flex");
          flag *= -1;
        }
      }
      pk = e.currentTarget.getAttribute(`data-pk`);
      const inputs = ["company", "name", "cellphone", "email", "value", "pk", "date", "tag", "notes"];
      inputs.forEach((input) => {
        $(`span[get-data=data-${input}]`).html(e.currentTarget.getAttribute(`data-${input}`));
      });
      $(`a[get-data=data-pk]`).attr("href", `/activities/call_scheduling/?pk=${e.currentTarget.getAttribute('data-pk')}`);
      $('#button_id').click(function (e){
        window.location.href= `/activities/call_popup/?pk=${pk}`
      })
      $('#call').click(function (e){
        
      });
      // history.pushState(null, '', `?pk=${pk}`);
    });
    
});