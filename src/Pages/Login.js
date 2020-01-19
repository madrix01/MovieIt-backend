import React,{ Component, useState } from 'react'
import LoginForm from '../Components/LoginForm'
import { Redirect } from 'react-router-dom';

class LoginUser{
    constructor(e,p){
        this.email = e;
        this.password = p;
    }
}
export default function Login() {

    var [state,setState] = useState()
    state = {
        islogged:false
    }


    async function login(event){
        event.preventDefault();
        console.log(event);

        let email = event.target.email.value;
        let password = event.target.password.value;
        let formBody = ""
        let details = ""
        try{
            email = "u9ee003@eed.os"
            password = "6484874633"
            if(email.length >= 6 && password.length >= 6){
                let User = new LoginUser(email,password);

                console.log(User);
                

               
                const response = await fetch("http://127.0.0.1:8000/api/login/",{
                    method:"POST",
                    headers:{
                        'Content-type':'application/x-www-form-urlencoded'
                    },
                    body:"email="+User['email']+"&"+"password="+User['password']
                })
                const data = await response.json()

                console.log(data)


                if(response.status === 200){
                    localStorage.setItem("token","true");
                    setState({
                        islogged:true
                    })
                }else{
                    localStorage.removeItem("token");
                }
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
           <div className='jumbotron'>
               <a className='display-4'> Please Login to Continue !</a>
               <div className='container'>
               <form onSubmit={login}>
            <div class="form-group">
              <label for="exampleInputEmail1" className='lead'>Email address</label>
              <input type="email" class="form-control" name='email' id="email" aria-describedby="emailHelp" placeholder="Enter email" />
              <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1" className='lead'>Password</label>
              <input type="password" class="form-control" name='password' id="password" placeholder="Password" />
            </div>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1" />
              <label class="form-check-label" for="exampleCheck1" className='lead'>Check me out</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
               </div>
           </div>
    
        )
    }
}
