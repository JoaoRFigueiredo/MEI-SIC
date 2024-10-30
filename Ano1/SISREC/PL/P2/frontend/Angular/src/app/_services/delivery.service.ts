import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Delivery } from '../_models/Delivery';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DeliveryService {
  constructor(private http: HttpClient) { }

  getDeliveries(): Observable<Delivery[]> {
    return this.http.get<Delivery[]>(environment.WAREHOUSE_URL_LOCAL + environment.DELIVERIES_URL, {observe: 'body', responseType: 'json'});
  }

  getDelivery(id: string): Observable<Delivery>{
    return this.http.get<Delivery>(environment.WAREHOUSE_URL_LOCAL  + environment.DELIVERIES_URL + "/" + id);
  }

  update(delivery: Delivery): Observable<any>{
    return this.http.put(environment.WAREHOUSE_URL_LOCAL + environment.DELIVERIES_URL + "/" + delivery.id,delivery);
  }

  addDelivery(delivery: any): Observable<Delivery>{
    return this.http.post<Delivery>(environment.WAREHOUSE_URL_LOCAL + environment.DELIVERIES_URL , delivery);
  }
}
