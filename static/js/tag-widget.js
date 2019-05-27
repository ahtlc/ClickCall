/* --- Settings and vars---*/
const tags = document.querySelector('#contact-tags');
const maxTags = 3; 
const APIEndpoint = '/activities/api/tags/';
const domSelectedTags = document.querySelector('#contact-tags > .selected-tags');
const domAvaliableTags = document.querySelector('#contact-tags > .avaliable-tags');
let editMode = false;
let avaliableTags = [];
let selectedTags = [];
let selectedTagsNumber = 0;

const updateTagLists = () => {
    avaliableTags = Array.prototype.map.call(domAvaliableTags.children, tag => {
        return tag.innerText;
    }); 
    selectedTags = Array.prototype.map.call(domSelectedTags.children, tag => {
        return tag.innerText;
    }); 
}

/* Changes the tag between selected and avaliable list */
const toggleTag = (tagElement) => {
    if(editMode === true){
        if(tagElement.parentElement.classList.contains('avaliable-tags') == true
           && tags.classList.contains('-blocked') == false){
            domSelectedTags.append(tagElement);
            selectedTagsNumber += 1;
            
            if(selectedTagsNumber == maxTags){
                tags.classList.add('-blocked');
            } 
        } else{
            if(tagElement.parentElement.classList.contains('selected-tags')){
                domAvaliableTags.append(tagElement); 
                selectedTagsNumber -= 1;
                if(selectedTagsNumber < maxTags){
                    tags.classList.remove('-blocked');
                }
            }
        }
        updateTagLists();
    }
}

/*
 * Opens the edit mode to edit the tag related 
 * lists locally.
 */
const editTags = () => {
    tags.classList.toggle('-expanded');
    editMode = !editMode;
}
