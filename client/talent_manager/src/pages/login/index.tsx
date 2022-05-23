import * as React from 'react';

import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';

const Login = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm">
        <Box sx={{ bgcolor: 'red', height: '100%' }} />
      </Container>
    </React.Fragment>
  );
}


export default Login;