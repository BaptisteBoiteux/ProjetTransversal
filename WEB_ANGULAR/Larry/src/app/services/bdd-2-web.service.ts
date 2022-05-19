import { Injectable } from '@angular/core';
import { Observable, Timestamp } from 'rxjs';
import { HttpClient } from '@angular/common/http';

const baseUrl = "http://localhost:8080/api/rondes"

@Injectable({
  providedIn: 'root'
})
export class Bdd2WebService {

  constructor(private http: HttpClient) { }
  private user = [{
    id: 1,
    login: "user",
    passwd: "user"
  },
  {
    id: 2,
    login: "root",
    passwd: "root"
  }
  ]

  private data = [{
    id: 1,
    heure: "23/05 - 8h45",
    temps: 12.4,
    nb_tab: 17,
    tab_presence: [1,0,0,1]
  },
  {
    id: 2,
    heure: "23/05 - 23h45",
    temps: 15.5,
    nb_tab: 12,
    tab_presence: [0,0,0,0]
  },
  {
    id: 3,
    heure: "23/05 - 18h54",
    temps: 19.3,
    nb_tab: 13,
    tab_presence: [1,0,1,1]
  },
  {
    id: 4,
    heure: "23/05 - 18h54",
    temps: 19.3,
    nb_tab: 13,
    tab_presence: [1,0,1,1]
  },
  {
    id: 5,
    heure: "23/05 - 18h54",
    temps: 19.3,
    nb_tab: 13,
    tab_presence: [1,0,1,1]
  },
  {
    id: 6,
    heure: "23/05 - 18h54",
    temps: 19.3,
    nb_tab: 13,
    tab_presence: [1,0,1,1]
  }
]
  public updateTabData() {
    //TO DO BAPTISTE
  }
  
  public updateUsrData() {
    //TO DO BAPTISTE
  }

  getAll(): Observable<any> {
    return this.http.get(baseUrl);
  }

  public getTabData(): {id:number, heure:string, temps:number, nb_tab:number, tab_presence:any}[] {
    return this.data;
  }

  public getUsrData(): {id:number, login:string, passwd:string}[] {
    return this.user;
  }
}
