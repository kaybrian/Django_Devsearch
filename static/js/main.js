

    
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm){
    for (let i=0;pageLinks.length >i; i++ ){
        pageLinks[i].addEventListener('click', function (e){
            e.preventDefault()
            //get the data attrs 
            let page = this.dataset.page
            
            //add the hidden search field to form 
            searchForm.innerHTML += `<input value=${page} name="page" hidden /> `

            // suubmit for 
            searchForm.submit()
        })
    }

}
