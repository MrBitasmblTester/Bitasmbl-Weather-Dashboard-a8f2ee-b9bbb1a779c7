const baseUrl = '/api';
export async function getCurrent(city:string){
  return fetch(`${baseUrl}/weather/current?city=${city}`);
}
