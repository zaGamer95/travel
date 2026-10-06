// Region tabs on the home page: All / Korea / Japan / Singapore / Other
(function () {
  var nav = document.querySelector(".tabs");
  if (!nav) return;
  var featured = nav.dataset.featured.split(" ");
  var cards = document.querySelectorAll("#trip-list .trip-card");
  var empty = document.getElementById("empty");

  function matches(card, filter) {
    var cs = card.dataset.countries.split(" ");
    if (filter === "all") return true;
    if (filter === "other") return cs.some(function (c) { return c && featured.indexOf(c) < 0; });
    return cs.indexOf(filter) >= 0;
  }

  function apply(filter) {
    var shown = 0;
    cards.forEach(function (card) {
      var ok = matches(card, filter);
      card.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
    nav.querySelectorAll("button").forEach(function (b) {
      b.classList.toggle("active", b.dataset.filter === filter);
    });
  }

  nav.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    apply(b.dataset.filter);
    history.replaceState(null, "", b.dataset.filter === "all" ? location.pathname : "#" + b.dataset.filter);
  });

  var initial = location.hash.slice(1);
  if (initial && nav.querySelector('[data-filter="' + initial + '"]')) apply(initial);
})();
