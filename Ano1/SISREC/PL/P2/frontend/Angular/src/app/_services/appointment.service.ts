import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Appointment } from 'src/app/_models/Appointment';
@Injectable({
  providedIn: 'root'
})
export class AppointmentService {

  constructor(private http: HttpClient) { }
  getAppointments(): Observable<Appointment[]> {
    return this.http.get<Appointment[]>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL);
  }
  createAppointment(appointment: Appointment): Observable<Appointment> {
    console.log("service creatappointment angular")
    return this.http.post<Appointment>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL + "/create", appointment);
  }
  getAppointmentsFromPlace(place: string): Observable<Appointment[]> {
    return this.http.get<Appointment[]>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL + "/" + place);
  }
  getAppointmentsFromClient(email: string): Observable<Appointment[]> {
    return this.http.get<Appointment[]>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL + "/client/" + email);
  }
  getAppointmentsFromPlaceAndBarber(place: string, accountable: string): Observable<Appointment[]> {
    return this.http.get<Appointment[]>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL + "/" + place + "/" + accountable);
  }
  deleteAppointment(day: string, place: string, email: string, accountable: string, type: string): Observable<boolean> {
    console.log("delete appointment angular");
    console.log("type -> " + type);
    const body = {
      day: day,
      place: place,
      accountable: accountable,
      email: email,
      type: type
    };
    return this.http.post<boolean>(environment.LOGISTICS_URL_LOCAL + environment.APPOINTMENTS_URL + "/delete/",body );
  }
}