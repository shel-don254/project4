import React, {  useState } from "react";
function Form() {
    const [password, setPassword] = useState('');
    const [username, setUserName] = useState('');
    const [mode, setMode] = useState('login'); 
    const [authenticated, setAuthenticated] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      if (mode === 'login') {
       
        try {
          
          const response = await fetch('/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
          });
  
          if (response.status === 200) {
            setAuthenticated(true);
          } else {
            setAuthenticated(false);
          }
        } catch (error) {
          console.error('Login failed:', error);
        }
      } else if (mode === 'signup') {

        try {        
         
          const response = await fetch('/signup', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
          });
  
          if (response.status === 201) {
            setMode('login');
          } else {
            
          }
        } catch (error) { 
          console.error('Sign-up failed:', error);
        }
      }
    };
  
    return (
      <div className="App">
        
  
        <div className="content-overlay">
          <h1>Welcome, User!loading...</h1>
          {authenticated ? (
            <div>
              <h2> </h2>
            </div>
          ) : (
            <div>
              <h2>{mode === 'login' ? 'Login' : 'Sign Up'}</h2>
              <form onSubmit={handleSubmit}>
                  <div>
                    <label>Name:</label>
                    <input
                      type="text"
                      value={username}
                      onChange={(e) => setUserName(e.target.value)}
                      required
                    />
                  </div>
                
                  <div>
                  <label>Password:</label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                <button type="submit">{mode === 'login' ? 'Login' : 'Sign Up'}</button>
              </form>
              {mode === 'login' ? (
                <p>
                  Don't have an account?{' '}
                  <button onClick={() => setMode('signup')}>Sign Up</button>
                </p>
              ) : (
                <p>
                  Already have an account?{' '}
                  <button onClick={() => setMode('login')}>Login</button>
                </p>
              )}
            </div>
          )}
        </div>
      </div>
    );
  }
  
  export default Form;
  