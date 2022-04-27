import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-historique',
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.scss']
})
export class HistoriqueComponent implements OnInit {
  data = [{
    id: 1,
    heure: "23/05 - 8h45",
    temps: 12.4,
    nb_tab: 12
  },
  {
    id: 2,
    heure: "23/05 - 23h45",
    temps: 15.5,
    nb_tab: 12
  },
  {
    id: 3,
    heure: "23/05 - 18h54",
    temps: 19.3,
    nb_tab: 13
  }
]
  constructor() { }

  ngOnInit(){
    //this.data = this.getData();
  }

  test(): void {
    console.log("appel de la fonction test du component historique"); 
  }

  getData(){
    console.log("search data into database")
  }
}