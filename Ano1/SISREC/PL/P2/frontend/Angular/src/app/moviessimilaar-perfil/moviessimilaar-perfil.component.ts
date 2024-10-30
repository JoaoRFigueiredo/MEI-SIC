import { Component } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { HttpClient } from '@angular/common/http';
import { Movie } from '../_models/Movie';

@Component({
  selector: 'app-moviessimilaar-perfil',
  templateUrl: './moviessimilaar-perfil.component.html',
  styleUrls: ['./moviessimilaar-perfil.component.css']
})
export class MoviessimilaarPerfilComponent {
  isDropdownOpen: boolean = false;
  searchQuery: string = '';
  movies: any[] = [];
  personalizedMovies: any [] =[];
  personalizedMoviesContent: any [] =[];
  personalizedMoviesCollaborative: any [] =[];
  filteredMovies: any[] = [];
  isLoading: boolean = false;
  error: string | null = null;
  rating: number = 0;
  title: any ='';
  selectedMovie: Movie | null = null; // Inicializando como null
  idMovie=this.selectedMovie?.movie_id;
  constructor(private http: HttpClient, private authservice:AuthService) {}

  ngOnInit() {
    this.getPersonalizedCollaborativeMovies();

  }
  getPersonalizedCollaborativeMovies(){
    this.authservice.getPersonalizedCollaborative(this.authservice.getUserId()).subscribe(
      (cmovies: Movie[]) => {
        this.personalizedMoviesCollaborative = cmovies;
      },
      (error) => {
        console.error('Erro ao obter filmes personalizados:', error);
        this.error = 'Ocorreu um erro ao obter filmes personalizados. Tente novamente mais tarde.';
      }
    );
    console.log(this.personalizedMoviesCollaborative)
  }
  selectMovie(movie: any) {
    console.log('Movie selected:', movie);
    this.selectedMovie = movie; // Atualizando o selectedMovie com o filme selecionado
    console.log(this.selectedMovie?.url)
    this.getTitle();
    this.getPersonalizedContentMovies();
    console.log("title ->"+movie.title);
    console.log("MovieId ->->"+movie.MovieId);
    console.log("year->"+movie.year);
    console.log("movie_id"+movie.movie_id)
    
  }
  getTitle(){
    this.title= this.selectedMovie?.title;
    console.log(this.title)
  }
  getPersonalizedContentMovies(){
    this.authservice.getPersonalizedContent(this.authservice.getUserId(),this.title).subscribe(
      (lmovies: Movie[]) => {
        this.personalizedMoviesContent = lmovies;
      },
      (error) => {
        console.error('Erro ao obter filmes personalizados:', error);
        this.error = 'Ocorreu um erro ao obter filmes personalizados. Tente novamente mais tarde.';
      }
    );
    console.log(this.personalizedMoviesContent)
  }
}