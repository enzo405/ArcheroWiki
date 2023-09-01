function cookieInitialize(){
    document.cookie = "windowInnerHeight=" + window.innerHeight +  "; path=/";
    document.cookie = "windowInnerWidth=" + window.innerWidth +  "; path=/";
}
cookieInitialize()

function createModale(element, urlNeedParentid, type){
    var titremodals = "";
    var url = window.location.href
    if(element.nodeType === Node.ELEMENT_NODE){
        titremodals = document.createElement("h3");
        titremodals.innerHTML = `<a href='${url}'>${element.parentElement.id}</a>`;
        if(urlNeedParentid == true){
            url = url.split('?')[0]
            titremodals.innerHTML = `<a href='/wiki/menu/${element.parentElement.id}/' target="_blank">${(element.parentElement.id).replaceAll('_',' ').toUpperCase()}</a>`;
            navigator.clipboard.writeText(`https://stats.wiki-archero.com/wiki/menu/${element.parentElement.id}/`)
        }else{
            titremodals.innerHTML = `<a href='${url}'>${element.parentElement.id}</a>`;
            navigator.clipboard.writeText(url)
        }
    }else{
        titremodals = document.createElement("h4");
        titremodals.innerHTML = element;
    }
    const modals = document.createElement("div");
    modals.classList.add("modals");
    const contenumodals = document.createElement("div");
    contenumodals.classList.add(`${type}-messages`);
    contenumodals.classList.add(`modals-contenu`);
    contenumodals.appendChild(titremodals);
    const boutonFermer = document.createElement("button");
    boutonFermer.textContent = "Close";
    boutonFermer.addEventListener("click", () => {
        document.body.removeChild(modals);
    });
    contenumodals.appendChild(boutonFermer);
    modals.appendChild(contenumodals);
    document.body.appendChild(modals);
    setTimeout(function(){
        modals.style.opacity = 0;
        setTimeout(function() {
            try{
                document.body.removeChild(modals);
            }catch{}
        }, 5000);
    }, 5000);
}