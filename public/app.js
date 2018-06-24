

document.addEventListener("DOMContentLoaded", event => {
    

    const app = firebase.app();
    const db = firebase.firestore();
    console.log(app);
    var username = sessionStorage.getItem("username");
    if(username != null && username != undefined){
        document.getElementById("loginButton").style.visibility = 'hidden';
        document.getElementById("user").innerText = "Hello "+username;
        document.getElementById("on").style.visibility = 'visible';
        document.getElementById("off").style.visibility = 'visible';

        
        
        const mypost = db.collection('deviceControl').doc('light');

        mypost.onSnapshot(doc => {
            const data = doc.data();
            //document.write(`Switch is :`+ data.status);
            document.getElementById("status").innerText = "Light Switch is  "+data.status;
        })
    }

});

function googleLogin(){
    const provider = new firebase.auth.GoogleAuthProvider();

    firebase.auth().signInWithPopup(provider)
        .then(result => {
            const user = result.user;
            document.write(`Hello ${user.displayName}`);
            console.log(user)
            sessionStorage.setItem("username",`${user.displayName}`);
        })
        .catch(console.log)
}

function switchOnOff(e){
    console.log(e);
    const db = firebase.firestore();
    const onOffPost = db.collection('deviceControl').doc('light');
    onOffPost.update({status : e});
}
