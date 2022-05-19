import { Component, forwardRef, Host, Inject, OnInit } from '@angular/core';
import { Bdd2WebService } from '../services/bdd-2-web.service';
import { AppComponent } from '../app.component';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})

export class ConnexionComponent implements OnInit {
  constructor(private bddService: Bdd2WebService,
             @Host() private _parent: AppComponent) { }

  ngOnInit(): void {
    this.bddService.getAllUsr();
    //console.log(this.userData)
  }

  onSubmit(login:string, password:string) {
    this.bddService.postUsr({"login":login,"password":password}).subscribe(val => {
      if(val){
        this._parent.setConnected()
        this._parent.setName(login.split(".")[0])}
    }
      );
  }
}
