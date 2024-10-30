import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Path } from '../_models/Path';
import { Planning } from '../_models/Planning';
import { Packaging } from '../_models/Packaging';
import { environment } from 'src/environments/environment';
import { GeneticPlanning } from '../_models/GeneticPlanning';
import { Travel } from '../_models/Travel';

@Injectable({
  providedIn: 'root'
})
export class LogisticsService {
  constructor(private http: HttpClient) { }

  getPaths(): Observable<Path[]> {
    return this.http.get<Path[]>(environment.LOGISTICS_URL_LOCAL + environment.PATHS_URL, { responseType: 'json' });
  }
  public getSpecificPath(id: string): Observable<any> {
    return this.http.get(environment.LOGISTICS_URL_LOCAL + environment.PATHS_URL + '/' + id, { responseType: 'text'});
  }

  postPath(path: any): Observable<Path> {
    console.log(environment.LOGISTICS_URL_LOCAL + environment.PATHS_URL);
  
    console.log(path);
    return this.http.post<Path>(environment.LOGISTICS_URL_LOCAL + environment.PATHS_URL, path);
  }

  getTravels(): Observable<Travel[]> {
    return this.http.get<Travel[]>(environment.LOGISTICS_URL_LOCAL + environment.TRAVEL_URL, { responseType: 'json' });
  }

  getPlanning(truckId: string, date: string): Observable<Planning> {
    return this.http.get<Planning>(environment.LOGISTICS_URL_LOCAL + environment.PLANNING_URL + '/' + truckId + '/' + date, { responseType: 'json' });
  }




  getGeneticPlanning(geneticplanning:GeneticPlanning):Observable<String>{
    console.log(geneticplanning);
    console.log("date"+geneticplanning.date);
    console.log("numero geracoes"+geneticplanning.nrgeracoes);
    console.log("tamanho populacao"+geneticplanning.tamanhopop);
    console.log("probcruzamento"+geneticplanning.probcruzamento);
    console.log("probmutacao"+geneticplanning.probmutacao);
    //console.log("termino is"+termino);
    
    return this.http.post<String>(environment.LOGISTICS_URL_LOCAL + environment.GENETICPLANNING_URL , geneticplanning);
  }
  //Packaging packaging
  getPackagings(): Observable<Packaging[]> {
    return this.http.get<Packaging[]>(environment.LOGISTICS_URL_LOCAL + environment.PACKAGING_URL, { responseType: 'json' });
  }

  getPackaging(id: string): Observable<Packaging> {
    return this.http.get<Packaging>(environment.LOGISTICS_URL_LOCAL + environment.PACKAGING_URL + '/' + id, { responseType: 'json'});
  }

  postPackaging(info: any): Observable<Packaging> {
    return this.http.post<Packaging>(environment.LOGISTICS_URL_LOCAL + environment.PACKAGING_URL, info);
  }
  putPackaging(info: any): Observable<Packaging> {
    return this.http.put<Packaging>(environment.LOGISTICS_URL_LOCAL + environment.PACKAGING_URL, info);
  }
 
}