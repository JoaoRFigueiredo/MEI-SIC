// favorite-movies.component.ts

import { Component } from '@angular/core';
import { AppointmentService } from '../_services/appointment.service';
import { AuthService } from '../_services/auth.service';
import { Movie } from '../_models/Movie';
import { Router } from '@angular/router';

@Component({
  selector: 'app-favorite-movies',
  templateUrl: './favorite-movies.component.html',
  styleUrls: ['./favorite-movies.component.css']
})
export class FavoriteMoviesComponent {

  searchTerm: string = '';
  favoriteMovies: any[] = [];
  barbeirosFiltrados: any[] = [];
  favoritos: string[] = [];
  userEmail = this.authService.getUserEmail();
  marcacaoCancelada: boolean = false;

  constructor(private appointmentService: AppointmentService, private authService: AuthService, private router:Router) { }

  ngOnInit() {
    this.carregarFavoriteMovies();
    console.log("future appoitnments ->" + this.favoriteMovies)
  }
  carregarFavoriteMovies() {
    this.userEmail = this.authService.getUserEmail();
    this.authService.getFavorites(this.userEmail).subscribe(
      (movies: string[]) => {
        this.favoriteMovies = movies;
        console.log("favorite Movies -> "+ this.favoriteMovies);

      },
      error => {
        console.error('Erro ao carregar os filmes favoritos:', error);
      }
    );
  }
  cancelarCompromisso(day: string, place: string, email: string, accountable: string, type: string) {
    this.appointmentService.deleteAppointment(day, place, email, accountable, type).subscribe(
      () => {
        this.marcacaoCancelada = true;
      },
      error => {
        console.error('Erro ao cancelar a marcação:', error);
      }
    );
    setTimeout(() => {
      //this.router.navigate(['/profile']);
    }, 2300); 
  }
  goBack(){
    this.router.navigate(['/profile'])
  }
}
