//Prompt
function Menu(){

    this.start = MenuStart;
    this.mainMenu = MenuMainMenu;
}

function MenuStart(){
    var option = true;

    while(option){

        if(this.mainMenu == 5){
            option = false;
        }
    }
}

function MenuMainMenu(){
    stringMenu = ""
    var selection = prompt(stringMenu);
    return selection;
}