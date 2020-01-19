import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'
const Cards = ()=>{
  return(
    <div class="card" style="width: 18rem;">
      <img src="..." class="card-img-top" alt="..." />
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">Cras justo odio</li>
        <li class="list-group-item">Dapibus ac facilisis in</li>
        <li class="list-group-item">Vestibulum at eros</li>
      </ul>
      <div class="card-body">
        <a href="#" class="card-link">Card link</a>
        <a href="#" class="card-link">Another link</a>
      </div>
    </div>
);
}
export default function Home() {
  var [ state,setState ] = useState();

    state = {
      genres:[
        {name:"Adventure",status:false},
        {name:"Action",state:false},
        {name:"Crime",state:false},
        {name:"Fantasy",state:false},
        {name:"Family",state:false},
        {name:"Comedy",state:false},
        {name:"Romance",state:false},
        {name:"Horror",state:false},
        {name:"Thriller",state:false},
        {name:"animation",state:false},
        {name:"Drama",state:false}
      ],
      isgenres:false,
      isResults:false,
      Results:[]
    }
  if(1){
    // localStorage.getItem("token") && localStorage.getItem("token") === "true"
    
   let genres = [
    {name:"Adventure",status:false},
    {name:"Action",state:false},
    {name:"Crime",state:false},
    {name:"Fantasy",state:false},
    {name:"Family",state:false},
    {name:"Comedy",state:false},
    {name:"Romance",state:false},
    {name:"Horror",state:false},
    {name:"Thriller",state:false},
    {name:"animation",state:false},
    {name:"Drama",state:false}
  ]

  let tosendgenres = [];
  let formbody = '';
  async function getMovies(event){
    event.preventDefault();
    if(state.isgenres == false){

      console.log("Search by String !")
      let name = event.target.movie.value;

      fetch('http://127.0.0.1:8000/api/search/',{
        method:"POST",
        headers:{
          'Content-type':'application/x-www-form-urlencoded'
        },
        body:"search="+name
      })
      .then(res=>res.json().then(data=>{
        console.log(data)
        this.setState({
          isResults:true,
          Results:data
        })

      }))

    }else{
      console.log("Selected Genres - ",tosendgenres)
  tosendgenres = encodeURI(tosendgenres);
  console.log(tosendgenres);

    fetch('http://127.0.0.1:8000/api/genre/',{
      method:"POST",
      headers:{
        'Content-type':'application/x-www-form-urlencoded'
      },
      body:tosendgenres
    })
    .then(reponse => reponse.json().then(data=>{
      console.log(data)
      tosendgenres = [];

    }))
    .catch(err=>{
      console.log(err);
      tosendgenres = [];

    })
    }
  }
  function changeState(event){

    setState({
      isgenres:true
    })

    for(let i = 0; i<10; i++){
      if(state.genres[i].name == event.target.value){
          tosendgenres.push(event.target.value)
      }
    }

    
  }
    return (<div className="jumbotron">
    <h1 className="display-4">Let's get some Recommendation !</h1><br />
    <form onSubmit={getMovies}>
 <div className="container">
 <div className="form-group row">
    <div className="col-sm-9">
      <input style={{
        fontSize:'25px',
        margin:0
      }} type="text" className="form-control" id="movie" name='movie' placeholder="Enter Movie Name" />
    </div>
    <div className="col-sm-3" style={{margin:0}}>
    <button style={{
        fontSize:'25px'
      }}  className='btn btn-block btn-success waves-effect waves-light'>Search</button>
    </div>
  </div>
 </div>
  <fieldset className="form-group"><a className="lead" style={{fontSize:'2.5rem'}}>Or, <br />Why don't you go by filters !</a><br /><br />
    <div className="row">
      
    
      <div className="col-sm-12" style={{display:'inline-flex'}}>
        {
          genres.map(movie => <div key={movie.name} onClick={changeState} className="form-check">
          <input className="form-check-input"  type="hidden" name="genres" id='genres' value={movie.name} />
            <button type="button" className="btn btn-primary">
              {movie.name}
          </button>
        </div>)
        }
      </div>
    </div>
  </fieldset>
  
</form>
    
  </div>
    )
      }else{
    return(<Redirect to='/login' / >)
  }

   
}
