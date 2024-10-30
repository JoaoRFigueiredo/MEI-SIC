import { Component } from '@angular/core';
import { AppointmentService } from '../_services/appointment.service';
import { AuthService } from '../_services/auth.service';
import { Router } from '@angular/router';
import { Appointment } from '../_models/Appointment';

@Component({
  selector: 'app-past-ratings',
  templateUrl: './past-ratings.component.html',
  styleUrls: ['./past-ratings.component.css']
})
export class PastRatingsComponent {

  p: number = 1;
  searchTerm: string = '';
  pastRatings: Appointment[] = [];
  barbeirosFiltrados: any[] = [];
  favoritos: string[] = [];
  userEmail = this.authService.getUserEmail();

  constructor(private appointmentService: AppointmentService, private authService: AuthService, private router: Router) { }

  ngOnInit() {
    this.carregarPastRatings();
    console.log("past Ratings ->" + this.pastRatings)
  }

  carregarPastRatings() {
    // Obter os compromissos do cliente usando subscribe
    this.appointmentService.getAppointmentsFromClient(this.userEmail).subscribe(allAppointments => {
      // Obter a data atual
      const currentDate = new Date();

      // Filtrar os compromissos futuros
      this.pastRatings = allAppointments.filter(appointment => {
        const appointmentDate = new Date(appointment.day); // Certifique-se de que a propriedade 'day' existe no objeto do compromisso
        console.log("appointmentdate= " + appointmentDate)
        console.log("current date -> " + currentDate)
        return appointmentDate < currentDate;
      });
      this.pastRatings.reverse();
      console.log("past Ratings -> " + this.pastRatings)
    });
  }


}
