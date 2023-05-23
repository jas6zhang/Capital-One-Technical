import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

// pass setApiResponse function as prop
const DataUpload = ({ onApiResponse }) => {
  const [apiResponse, setApiResponse] = useState(null);

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    const reader = new FileReader();

    reader.onload = () => {
      const transactionData = JSON.parse(reader.result);
      
      // Send a POST request to the server with the transaction data
      axios.post('http://127.0.0.1:5000/calculate_rewards', transactionData)
        .then(response => {
          // Save the response in state
          setApiResponse(response.data);
          onApiResponse(response.data);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };
    reader.readAsText(file);
  }, [onApiResponse]); // call the setApiResponse function when the API response arrives

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
  
  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {
        isDragActive ? <h3>Drop the file here...</h3> : <h3>Drag and drop a file here, or click to select a file</h3>
      }
    </div>
  );
};

export default DataUpload;
