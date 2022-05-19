import { Component, OnInit } from '@angular/core';
import { Data } from '@angular/router';
import { Bdd2WebService } from '../services/bdd-2-web.service';

@Component({
  selector: 'app-historique',
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.scss']
  })
export class HistoriqueComponent implements OnInit {
  display_more = -1;
  data :     {id:number, heure:string, temps:number, nb_tab:number, tab_presence:string[]}[] = [];

  constructor(private bddService: Bdd2WebService) { }

  ngOnInit(){
    this.bddService.getAllRde().subscribe(val => this.data=val);
  }
}
