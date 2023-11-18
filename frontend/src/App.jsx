import "./App.css"
import { Spinner } from "@chakra-ui/react"

function App() {
  return (
    <Spinner
      thickness='5px'
      speed='1s'
      emptyColor='gray.200'
      color='blue.500'
      size='xl'
    />
  )
}

export default App
