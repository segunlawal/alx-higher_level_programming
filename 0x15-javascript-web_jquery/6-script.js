const header = $("header");
const addDiv = $("div#update_header");

addDiv.on("click", () => {
  header.text("New Header!!!");
});
