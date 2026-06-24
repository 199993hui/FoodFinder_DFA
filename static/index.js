$(document).ready(function () {
  $(".ajax").click(function () {
    $.ajax({
      url: "/transition",
      type: "get",
      data: { word: $(".select").val() },
      success: function (response) {
        const json = response.states;
        const accept = response.accept;

        if (json["-1"]) {
          let trap_state = json["-1"];
          let next_state = Object.entries(json).filter(([state]) => state !== "-1");
          trap_state = Object.entries(trap_state).map(([state, _]) => ["-1", _]);
          let transition = [...next_state, ...trap_state];
          let transition_state = transition.map(([state, successor]) => `
            <tr>
              <td>${state}</td>
              <td>${successor.char}</td>
              <td>${successor.next_state}</td>
            </tr>`);
          let transition_table = `
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Current State</th>
                  <th>Input</th>
                  <th>Next State</th>
                </tr>
              </thead>
              <tbody>${transition_state.join("")}</tbody>
            </table>
            <div class="d-flex align-items-center">
              <p class="fw-bold mb-0 p-2">Status</p>
              <span class="badge text-bg-danger">Rejected</span>
            </div>`;
          $(".transition_table").html(transition_table);
        } else {
          let length = Object.entries(json).length;
          let isAccepted = accept.includes(Object.entries(json)[length - 1][1].next_state);
          let badge = isAccepted
            ? `<span class="badge text-bg-success">Accepted</span>`
            : `<span class="badge text-bg-danger">Rejected</span>`;
          let rows = Object.entries(json).map(([state, next]) => `
            <tr>
              <td>${state}</td>
              <td>${next.char}</td>
              <td>${next.next_state}</td>
            </tr>`);
          let transition_table = `
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Current State</th>
                  <th>Input</th>
                  <th>Next State</th>
                </tr>
              </thead>
              <tbody>${rows.join("")}</tbody>
            </table>
            <div class="d-flex align-items-center">
              <p class="fw-bold mb-0 p-2">Status</p>
              ${badge}
            </div>`;
          $(".transition_table").html(transition_table);
        }
      },
    });
  });
});
