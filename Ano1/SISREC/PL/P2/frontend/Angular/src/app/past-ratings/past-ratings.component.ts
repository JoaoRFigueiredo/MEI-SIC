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
  barbeirosFiltrados: any[] = [];
  favoritos: string[] = [];
  pastRatings: any[] = [];

  userEmail = this.authService.getUserEmail();

  constructor(private appointmentService: AppointmentService, private authService: AuthService, private router: Router  ) { }

  ngOnInit() {
    this.carregarPastRatings();
    console.log("past Ratings ->" + this.pastRatings)
  }

  carregarPastRatings() {
    this.authService.getHistoryRatings().subscribe(
      (movies: string[]) => {
        this.pastRatings = movies;
        console.log("past ratings -> " + this.pastRatings);
      },
      error => {
        console.error('Erro ao carregar os filmes favoritos:', error);
      }
    );

  }
  goBack() {
    this.router.navigate(['/profile'])
  }
}
