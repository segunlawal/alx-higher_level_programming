const add_div = $("DIV#add_item");

add_div.on("click", () => {
  $("ul.my_list").append("<li>Item</li>");
});
