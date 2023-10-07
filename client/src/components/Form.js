import React, {  useState } from "react";
function Form() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [mode, setMode] = useState('login'); // 'login' or 'signup'
    const [authenticated, setAuthenticated] = useState(false);
  
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      if (mode === 'login') {
        // Perform login logic here (make an API request)
        try {
          // Replace with actual API call to authenticate the user
          const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
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
        // Perform sign-up logic here (make an API request)
        try {
          // Replace with actual API call to register the user
          const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, password }),
          });
  
          if (response.status === 201) {
            setMode('login'); // Switch back to login mode after successful sign-up
            // You can optionally set a message indicating successful sign-up
          } else {
            // Handle sign-up error
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
              {/* Display authenticated content here */}
            </div>
          ) : (
            <div>
              <h2>{mode === 'login' ? 'Login' : 'Sign Up'}</h2>
              <form onSubmit={handleSubmit}>
                {mode === 'signup' && (
                  <div>
                    <label>Name:</label>
                    <input
                      type="text"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      required
                    />
                  </div>
                )}
                <div>
                  <label>Email:</label>
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
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
  