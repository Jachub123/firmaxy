galerie = document.querySelector(".galerieContainer")
bilder = document.querySelectorAll(".imgContainer")
document.addEventListener("DOMContentLoaded", () => {
    const viewport = window.innerWidth
    if(viewport < 992){
        return;
    }

for(let i = 0;i < bilder.length;i++){
    bilder[i].addEventListener("mouseenter", (e) => {
        if(e.target.classList.value.includes("imgContainer")){
            let leftSib = e.target.previousElementSibling
            let rightSib = e.target.nextElementSibling
            //EIN ITEM PRO REIHE
            //Sind die Siblings beide nicht auf der selben Höhe wie target
            try {
                leftSib.offsetTop            
            } catch (error) {                
                //ERSTES GALERIE-BILD
                //Wenn rechts einer ist und links keiner 
                if(e.target.offsetTop != rightSib.offsetTop){
                    console.log("DIESA HAT EIN ITEM PRO REIHE")
                    e.target.classList.add("thick") 
                }else{
                        
                    console.log("ERSTER BILD IN GALERIE")      
                    e.target.classList.add("thick")                
                    rightSib.classList.add("thin")       
                    if(e.target.offsetTop == rightSib.nextElementSibling){      
                        rightSib.nextElementSibling.classList.add("thin")    
                    }         
                    
                }
            }try {
                rightSib.offsetTop
            } catch (error) {
                //LETZTES GALERIE-BILD
                //Wenn rechts keiner ist und links einer   
                if(e.target.offsetTop != leftSib.offsetTop){
                    console.log("HUNNA EIN ITEM PRO REIHE")
                    e.target.classList.add("thick") 
                }
                 else{
                    e.target.classList.add("thick")                
                    leftSib.classList.add("thin")
                    if(e.target.offsetTop == leftSib.previousElementSibling){  
                        leftSib.previousElementSibling.classList.add("thin")
                    }
                } 
            }
            try{                
                if(e.target.offsetTop != leftSib.offsetTop && e.target.offsetTop != rightSib.offsetTop){
                    //EIN ITEM PRO REIHE
                    e.target.classList.add("thick")
                }  
            }catch (error) {}  
            
             

 
   
            //NICHT ERSTES OD. LETZTES GALERIE-BILD
            //Wenn rechts und links einer ist
            if(rightSib !== null && leftSib !== null){
                //LINKES BILD DER REIHER
                if(e.target.offsetTop === rightSib.offsetTop && e.target.offsetTop !== leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    rightSib.classList.add("thin")
                    if(e.target.offsetTop == rightSib.nextElementSibling.offsetTop){
                        rightSib.nextElementSibling.classList.add("thin")
                    }
                } 
                //RECHTES BILD DER REIHE
                else if(e.target.offsetTop !== rightSib.offsetTop && e.target.offsetTop === leftSib.offsetTop){
                    e.target.classList.add("thick")                
                    leftSib.classList.add("thin")
                    if(e.target.offsetTop == leftSib.previousElementSibling.offsetTop){
                        leftSib.previousElementSibling.classList.add("thin")
                    }
                }
                //MITTLERES BILD DER REIHE
                else if(e.target.offsetTop === rightSib.offsetTop && e.target.offsetTop === leftSib.offsetTop){
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
});