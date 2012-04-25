/*tinyMCE.init({
mode : "textareas",
theme : "simple"
});*/

tinyMCE.init({
	language : "es",
        mode : "exact",
        elements : "id_contenido",
        theme : "advanced",
        entity_encoding : "raw",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
	theme_advanced_blockformats : "p,div,h1,h2,h3,h4,h5,h6",
        theme_advanced_buttons1 : "formatselect,separator,bold,italic,underline,strikethrough,separator,bullist,numlist,separator,undo,redo,separator,link,unlink,anchor,separator,pastetext,pasteword,selectall,separator,cleanup,help,separator,table,separator,code",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        fix_nesting : true,
        relative_urls : false,
        auto_cleanup_word : true,
	paste_auto_cleanup_on_paste : true,
	paste_remove_styles : true,
	paste_remove_spans : true,
	paste_strip_class_attributes : true,
        plugins : "table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,searchreplace,print,paste,contextmenu,fullscreen",
        plugin_insertdate_dateFormat : "%m/%d/%Y",
        plugin_insertdate_timeFormat : "%H:%M:%S",
        extended_valid_elements : "a[name|href|title],img[class|src|alt|title|width|height],hr[class],span[class],#p",
	paste_preprocess : function(pl, o) {
            // Content string containing the HTML from the clipboard
            //alert(o.content);
        },
        paste_postprocess : function(pl, o) {
            // Content DOM node containing the DOM structure of the clipboard
            //alert(o.node.innerHTML);
        }

});
