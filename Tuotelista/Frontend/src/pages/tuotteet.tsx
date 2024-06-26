import axios from 'axios'

export const fetchTuotteet = async () => {

  try {
    const response = await  axios.get('http://localhost:8000/tuote/ReactView')
    return response.data
  }
  catch(error) {
    throw Error('Tuotelistaa ei löytynyt.')
  }
} 

export const muokkausLoader = async ({ params } : { params:any }) => {
  const { id } = params

  try {
    const response = await axios.get('http://localhost:8000/tuote/' + id )

    return response.data
  }

  catch(error) {
    throw Error('Tuotetta ei löytynyt.')
  }
}