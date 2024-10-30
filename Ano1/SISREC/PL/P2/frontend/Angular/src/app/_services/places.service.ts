import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Place } from 'src/app/_models/Place';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlacesService {

  constructor(private http: HttpClient) { }
  getPlaces(): Observable<Place[]> {
    return this.http.get<Place[]>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL );
  }
  getSolarios(): Observable<Place[]> {
    console.log("solarios service angular")
    return this.http.get<Place[]>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL + "/solarios");
  }
  getEsteticistas(): Observable<Place[]> {
    return this.http.get<Place[]>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL + "/esteticistas");
  }
  getCabeleireiros(): Observable<Place[]> {
    return this.http.get<Place[]>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL + "/cabeleireiros");
  }
  getBarbeiros(): Observable<Place[]> {
    return this.http.get<Place[]>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL + "/barbeiros");
  }
  getPlace(name: string): Observable<Place>{
    return this.http.get<Place>(environment.LOGISTICS_URL_LOCAL + environment.PLACES_URL + "/"+ name);
  }
}
