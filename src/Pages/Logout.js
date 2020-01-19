import React, { Component } from 'react'
import { Redirect } from 'react-router-dom'

export default class Logout extends Component {
    constructor(props){
        super(props)

        this.Logout();

    }
    async Logout(){
        console.log("Logout Inita")
        const response = await fetch('http://127.0.0.1:8000/api/logout/');
        const data = response.json()
        if(response.status === 200){
            localStorage.setItem("isMessage","true")
            localStorage.setItem("Message","Log Out Successfull")
            localStorage.removeItem("token");
            console.log("Logout Done with If")
        }else{
            console.log("Logout without if")
            localStorage.removeItem("token")
        }
    }



    render() {
        return (<Redirect to='/login' />)
    }
}
