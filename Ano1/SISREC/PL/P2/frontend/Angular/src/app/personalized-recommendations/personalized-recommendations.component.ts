import { Component } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { Movie } from '../_models/Movie';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-personalized-recommendations',
  templateUrl: './personalized-recommendations.component.html',
  styleUrls: ['./personalized-recommendations.component.css']
})
export class PersonalizedRecommendationsComponent {
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
  hasRated: boolean=false;
  selectedMovie: Movie | null = null; // Inicializando como null
  idMovie=this.selectedMovie?.movie_id;
  movieID: any = '';
  numberofrates=0;
  constructor(private http: HttpClient, private authservice:AuthService) {}

  ngOnInit() {
    this.getPersonalizedMovies();
    this.searchMovies();
  }
  getTitle(){
    this.title= this.selectedMovie?.title;
    console.log(this.title);
    
  }
  getPersonalizedMovies() {
    this.authservice.getPersonalizedHybrid(this.authservice.getUserId()).subscribe(
      (pmovies: Movie[]) => {
        this.personalizedMovies = pmovies;
      },
      (error) => {
        console.error('Erro ao obter filmes personalizados:', error);
        this.error = 'Ocorreu um erro ao obter filmes personalizados. Tente novamente mais tarde.';
      }
    );
    console.log(this.personalizedMovies)
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
  }

  searchMovies() {
    this.isLoading = true;
    this.filteredMovies = [];
    this.error = null;

    if (this.searchQuery.length >= 0) {
      this.authservice.getPersonalizedMovies(this.searchQuery)
        .subscribe({
          next: (data) => {
            this.movies = data as any[];

            this.filterMovies();
            this.isLoading = false;
          },
          error: (err) => {
            this.error = err.message;
            this.isLoading = false;
          },
        });
    } else {
      this.filteredMovies = [];
      this.isLoading = false;
    }
  }

  filterMovies() {
    this.filteredMovies = this.movies.filter((movie) => {
      const title = movie.title.toLowerCase();
      return title.includes(this.searchQuery.toLowerCase());
    });
  }

  selectMovie(movie: any) {
    this.hasRated=false;
    console.log('Movie selected:', movie);
    this.selectedMovie = movie; // Atualizando o selectedMovie com o filme selecionado
    console.log(this.selectedMovie?.url)
    this.getTitle();
    this.getPersonalizedContentMovies();
    this.movieID=movie.movieId;
    console.log("movieID ->"+this.movieID);
    console.log("title ->"+movie.title);
    console.log("genres ->"+movie.genres);
    console.log("titlelower ->"+movie.titlelower);

    console.log("MovieId ->->"+movie.MovieId);
    console.log("year->"+movie.year);
    console.log("movie_id"+movie.movie_id)
    console.log("id"+movie.id)
    console.log("id"+movie.movieId)


  }
  rateMovie(stars: number, movieId: number) {
    this.getPersonalizedMovies();

    this.hasRated= true;
    this.rating = stars;
    console.log(this.idMovie)
    console.log("fernando"+this.movieID)
    console.log("Estrelas -> " + stars);
    this.authservice.rate(stars, this.movieID).subscribe(
      (result) => {
        if (result) {
          console.log(result)
          console.log('Classificação enviada com sucesso!');
          // Faça algo aqui se a classificação for enviada com sucesso
        } else {
          console.error('Erro ao enviar classificação.');
          // Faça algo aqui se houver um erro ao enviar a classificação
        }
      },
      (error) => {
        console.error('Erro ao enviar classificação:', error);
        // Faça algo aqui se houver um erro na solicitação HTTP
      },
      () => {
        console.log('A solicitação de classificação foi concluída.');
        // Faça algo aqui após a conclusão da solicitação HTTP (opcional)
      }
    );
  }
  
  openDropdown() {
    this.isDropdownOpen = true;
  }

  closeDropdown() {
    this.isDropdownOpen = false;
  }
}
