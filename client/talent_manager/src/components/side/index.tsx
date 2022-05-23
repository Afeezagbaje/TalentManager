import * as React from 'react';

import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';

const Side = () => {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm" sx={{height: '90vh'}}>
        <Box sx={{ bgcolor: '#689D8D', height: '100%', borderRadius: "10px" }}></Box>
        
      </Container>
    </React.Fragment>
  );
}


export default Side;