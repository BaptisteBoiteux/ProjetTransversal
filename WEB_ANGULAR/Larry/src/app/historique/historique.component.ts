import { animate, style, transition, trigger } from '@angular/animations';
import { Component, OnInit } from '@angular/core';
import { Bdd2WebService } from '../services/bdd-2-web.service';

@Component({
  selector: 'app-historique',
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.scss']
  })
export class HistoriqueComponent implements OnInit {
  display_more = -1;
  data: {id:number, heure:string, temps:number, nb_tab:number, tab_presence:any}[] = []

  constructor(private bddService: Bdd2WebService) { }

  ngOnInit(){
    this.data = this.bddService.getTabData();
  }
}
