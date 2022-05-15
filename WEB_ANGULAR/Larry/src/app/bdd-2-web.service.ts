import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Bdd2WebService {

  constructor() { }

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
  public supdateData() {
    //TO DO BAPTISTE
  }

  public getData(): {id:number, heure:string, temps:number, nb_tab:number, tab_presence:any}[] {
    return this.data;
  }
}
