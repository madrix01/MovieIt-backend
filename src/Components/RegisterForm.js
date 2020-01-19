import React from 'react'
import { Redirect } from 'react-router-dom';

class RUser{
    constructor(e,p,u){
        this.email = e;
        this.password = p;
        this.username = u;
    }
}
export default function RegisterForm() {
    async function registerUser(event){
        event.preventDefault();
        console.log(event);

        let email = event.target.email.value;
        let password = event.target.password.value;
        let username = event.target.username.value;

        let formBody = ""
        let details = ""
        try{

            if(email.length >= 6 && password.length >= 6){
                let User = new RUser(email,password,username);

                console.log(User);


                const response = await fetch("http://127.0.0.1:8000/api/signup/",{
                    method:"POST",
                    headers:{
                        'Content-type':'application/x-www-form-urlencoded'
                    },
                    body:"email="+User['email']+"&"+"password="+User['password']+"&username="+User['username']
                })
                const data = await response.json()
                console.log(data)
            }else{
                throw {error:"Email and password must be > 6"}
            }
        }catch(err){
            console.log(err)
        }
    }
    if(localStorage.getItem("token") === "true"){
        return(<Redirect to='/home' />)
    }else{
        return (
            <form onSubmit={registerUser}>
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" class="form-control" id="email" name='email' aria-describedby="emailHelp" placeholder="Enter email" />
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputEmail1">Username</label>
        <input type="text" class="form-control" id="username" name="username" aria-describedby="emailHelp" placeholder="Enter email" />
        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input type="password" class="form-control" name='password' id="password" placeholder="Password" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
        )
    }
}
