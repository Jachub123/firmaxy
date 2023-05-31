galerie = document.querySelector(".galerieContainer")
bilder = document.querySelectorAll(".imgContainer")

for(let i = 0;i < bilder.length;i++){
    bilder[i].addEventListener("mouseenter", (e) => {
        let leftSib = e.target.previousElementSibling
        let rightSib = e.target.nextElementSibling
        if(e.target.classList.value.includes("imgContainer")){
            if(rightSib !== null && leftSib === null){            
                e.target.classList.add("thick")                
                rightSib.classList.add("thin")             
                rightSib.nextElementSibling.classList.add("thin")             
            }       
            else if(rightSib === null && leftSib !== null){
                if(e.target.offsetTop !== leftSib.offsetTop){
                    e.target.classList.add("thick")   
                } 
                if(e.target.offsetTop !== rightSib.offsetTop && e.target.offsetTop === leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    leftSib.classList.add("thin")
                    leftSib.previousElementSibling.classList.add("thin")
                }                            
            }       
            else if(rightSib !== null && leftSib !== null){
                if(e.target.offsetTop === rightSib.offsetTop && e.target.offsetTop !== leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    rightSib.classList.add("thin")
                    rightSib.nextElementSibling.classList.add("thin")
                } 
                if(e.target.offsetTop !== rightSib.offsetTop && e.target.offsetTop === leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    leftSib.classList.add("thin")
                    leftSib.previousElementSibling.classList.add("thin")
                } 
                if(e.target.offsetTop === rightSib.offsetTop && e.target.offsetTop === leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    leftSib.classList.add("thin")
                    rightSib.classList.add("thin")
                } 
            }       
            
        }
    });
    bilder[i].addEventListener("mouseleave", (e) => {
        for(let i = 0;i < bilder.length;i++){
            bilder[i].classList.remove("thick")
            bilder[i].classList.remove("thin")
        }
    });
}