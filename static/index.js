$(document).ready(function () {
  $(".ajax").click(function () {
    const word = $(".select").val().replace(/[<>"'&]/g, "");
    $.ajax({
      url: "/transition",
      type: "get",
      data: { word: word },
      success: function (response) {
        const json = response.states;
        const accept = response.accept;

        if (json["-1"]) {
          let trapState = json["-1"];
          let nextStates = Object.entries(json).filter(([state]) => state !== "-1");
          let trapRows = Object.entries(trapState).map(([_, val]) => ["-1", val]);
          let allRows = [...nextStates, ...trapRows];

          let rows = allRows.map(([state, successor]) => `
            <tr>
              <td>${state}</td>
              <td>${successor.char}</td>
              <td>${successor.next_state}</td>
            </tr>`).join("");

          $(".transition_table").html(`
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Current State</th>
                  <th>Input</th>
                  <th>Next State</th>
                </tr>
              </thead>
              <tbody>${rows}</tbody>
            </table>
            <div class="d-flex align-items-center">
              <p class="fw-bold mb-0 p-2">Status</p>
              <span class="badge text-bg-danger">Rejected</span>
            </div>`);
        } else {
          const entries = Object.entries(json);
          const lastNextState = entries[entries.length - 1][1].next_state;
          const isAccepted = accept.includes(lastNextState);

          let rows = entries.map(([state, next]) => `
            <tr>
              <td>${state}</td>
              <td>${next.char}</td>
              <td>${next.next_state}</td>
            </tr>`).join("");

          const badge = isAccepted
            ? `<span class="badge text-bg-success">Accepted</span>`
            : `<span class="badge text-bg-danger">Rejected</span>`;

          $(".transition_table").html(`
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Current State</th>
                  <th>Input</th>
                  <th>Next State</th>
                </tr>
              </thead>
              <tbody>${rows}</tbody>
            </table>
            <div class="d-flex align-items-center">
              <p class="fw-bold mb-0 p-2">Status</p>
              ${badge}
            </div>`);
        }
      },
    });
  });
});
