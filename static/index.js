$(document).ready(function () {
  $(".ajax").click(function () {
    $.ajax({
      url: "",
      type: "get",
      data: { word: $(".select").val() },
      contentType: "application/json",
      success: function (response) {
        const json_response = JSON.parse(response);
        const json = json_response.states
        const accept = json_response.accept
        console.log(accept)
        console.log(json)
        if (json["-1"]) {
          let trap_state = json["-1"];
          let next_state = Object.entries(json).filter(
            ([state]) => state !== "-1"
          );
          trap_state = Object.entries(trap_state).map(([state, _]) => [
            "-1",
            _,
          ]);
          let transition = [...next_state, ...trap_state];
          console.log(transition);
          let transition_state = transition.map(([state, successor]) => {
            return `
            <tr>
            <td>${state}</td>
            <td>${successor.char}</td>
            <td>${successor.next_state}</td>
            </tr>
            `;
          });
          let transition_table = `
            <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col">Current State</th>
                <th scope="col">Input</th>
                <th scope="col">Next State</th>
                </tr>
            </thead>
            <tbody>
                ${transition_state.join("")}
            </tbody>
            </table>
            <div class = "d-flex align-items-center">
            <p class="fw-bold mb-0 p-2">Status</p>
            <span class="badge text-bg-danger">rejected</span>
            </div>`;
          $(".transition_table").html(transition_table);
        } else {
            let table;
            console.log(json)
            let length = Object.entries(json).length
            if (
              accept.includes(Object.entries(json)[length - 1][1].next_state)
            ) {
              table = `<div class = "d-flex align-items-center">
                <p class="fw-bold mb-0 p-2">Status</p>
                <span class="badge text-bg-success">Accepted</span>
                </div>`;
            } else {
              table = `<div class = "d-flex align-items-center">
                <p class="fw-bold mb-0 p-2">Status</p>
                <span class="badge text-bg-danger">Rejected</span>
                </div>`;
            }
            let next_transition = Object.entries(json).map(
                ([state, next]) => `<tr>
                    <td>${state}</td>
                    <td>${next.char}</td>
                    <td>${next.next_state}</td>
                </tr>`);
                let transition_table = `<table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">current state</th>
                            <th scope="col">input</th>
                            <th scope="col">next state</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${next_transition.join("")}

                    </tbody>
                </table>
                ${table}`;
                $('.transition_table').html(transition_table)
            }
      },
    });
  });
});
