import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgxPaginationModule } from 'ngx-pagination';
import { MatIconModule } from '@angular/material/icon';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './board-admin/register/register.component';
import { BoardAdminComponent } from './board-admin/board-admin.component';
import { authInterceptorProviders } from './_helpers/auth.interceptor';
import { UsersComponent } from './users/users.component';
import { BoardClientComponent } from './board-client/board-client.component';
import { TesteComponent } from './teste/teste.component';
import { BoardEmployeeComponent } from './board-employee/board-employee.component';
import { RegisterEmployeeComponent } from './register-employee/register-employee.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { DisableEmployeeComponent } from './disable-employee/disable-employee.component';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { ExemploestabelecimentoComponent } from './estabelecimentosespecificos/exemploestabelecimento/exemploestabelecimento.component';
import { FavoritosComponent } from './favoritos/favoritos.component';
import { DescriptionExampleComponent } from './Descriptions/description-example/description-example.component';
import { MatDialogModule } from '@angular/material/dialog';
import { ProfileComponent } from './profile/profile.component';
import { FavoriteMoviesComponent } from './favorite-movies/favorite-movies.component';
import { PastRatingsComponent } from './past-ratings/past-ratings.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { AccountSettingsComponent } from './account-settings/account-settings.component';
import { MatButtonModule } from '@angular/material/button';
import { UserLoginComponent } from './user-login/user-login.component';
import { FormsModule } from '@angular/forms';
import { PersonalizedRecommendationsComponent } from './personalized-recommendations/personalized-recommendations.component';
import { FavoriteGenresComponent } from './favorite-genres/favorite-genres.component';
import { MoviessimilaarPerfilComponent } from './moviessimilaar-perfil/moviessimilaar-perfil.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    BoardAdminComponent,
    UsersComponent,
    BoardClientComponent,
    TesteComponent,
    BoardEmployeeComponent,
    RegisterEmployeeComponent,
    ReservationsComponent,
    DisableEmployeeComponent,
    ExemploestabelecimentoComponent,
    FavoritosComponent,
    DescriptionExampleComponent,
    ProfileComponent,
    FavoriteMoviesComponent,
    PastRatingsComponent,
    AccountSettingsComponent,
    UserLoginComponent,
    PersonalizedRecommendationsComponent,
    FavoriteGenresComponent,
    MoviessimilaarPerfilComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NgxPaginationModule,
    MatInputModule,
    MatIconModule,
    MatCardModule,
    MatDialogModule,
    MatFormFieldModule,
    MatButtonModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [authInterceptorProviders],
  bootstrap: [AppComponent] // Adicione o AppComponent ao array bootstrap
})
export class AppModule { }
