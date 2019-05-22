/* --- --- */
const tagWidget = $("contact-tags");

/* --- Settings ---*/
const maxTags = 3; 
const APIEndpoint = "/activities/api/tags/";

/* --- Lists ---*/
const domSelectedTags = document.querySelector("#contact-tags > .selected-tags").children;
const selectedTags = Array.prototype.map.call(domSelectedTags, tag => {
    return tag.innerText;
}); 

const domAvaliableTags = document.querySelector("#contact-tags > .avaliable-tags").children;
const avaliableTags = Array.prototype.map.call(domAvaliableTags, tag => {
    return tag.innerText;
}); 

/* Changes the tag between selected and avaliable list */
const toggleTag = (tagElement) => {
    
}

/* 
 * Makes a AJAX GET request to get the tags list 
 * from the tags API endpoint and returns a list
 * with the parsed data
 */
const getTagList = () => {
}

/*
 * Opens the edit mode to edit the tag related 
 * lists locally.
 */
const editTags = () => {
}

/* 
 * Makes a AJAX PUT with the updated content
 * to the tags API endpoint
 *
 */
const saveModifications = () => {
}
