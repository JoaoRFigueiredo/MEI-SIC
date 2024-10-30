import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Truck } from '../_models/Truck';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FleetService {
  constructor(private http: HttpClient) { }

  getTrucks(): Observable<Truck[]> {
    return this.http.get<Truck[]>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL, { responseType: 'json' });
  }

  getActiveTrucks(): Observable<Truck[]> {
    return this.http.get<Truck[]>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL + '/enabled', { responseType: 'json' });
  }

  getInactiveTrucks(): Observable<Truck[]> {
    return this.http.get<Truck[]>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL + "/disabled", { responseType: 'json' });
  }

  getTruck(id: string): Observable<Truck> {
    return this.http.get<Truck>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL + '/' + id, { responseType: 'json' });
  }

  postTruck(info: any): Observable<Truck> {
    return this.http.post<Truck>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL, info);
  }

  putTruck(info: any): Observable<Truck> {
    return this.http.put<Truck>(environment.LOGISTICS_URL + environment.TRUCKS_URL, info, { responseType: 'json' });
  }

  patchTruck(info: any): Observable<Truck> {
    return this.http.patch<Truck>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL, info, { responseType: 'json' });
  }

  deleteTruck(info: string): Observable<Truck> {
    return this.http.delete<Truck>(environment.LOGISTICS_URL_LOCAL + environment.TRUCKS_URL + '/' + info, { responseType: 'json' });
  }
}

