#################################################
Angularチュートリアル
#################################################
Last Updated on |date|

.. |date| date::

.. tip:: 本ページは、`ツアー・オフ・ヒーローズ <https://angular.jp/tutorial>`_ に沿って体験したときのメモです。詳細は本家参照願います。

新規プロジェクトの作成
============================================
新規アプリ生成
--------------------------------------------

ng new で実行::

  ng new angular-tour-of-heroes

アプリのサーブ
--------------------------------------------

ワークスペースに移動し、アプリケーションを起動::

  cd angular-tour-of-heroes
  ng serve --open

.. note:: --openフラグにより、http://localhost:4200が自動で開く。ここまでは入門編でも体験済み

アプリタイトルの変更
--------------------------------------------

app.component.ts (class title property)::

  title = 'Tour of Heroes';

.. code-block:: TypeScript
  :caption: app.component.ts (class title property)
  :linenos:
  :emphasize-lines: 9
  
  import { Component } from '@angular/core';

  @Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
  })
  export class AppComponent {
    title = 'Tour of Heroes'; // ここを変更してみる
  }

.. code-block:: html
  :caption: app.component.html (template)
  :linenos:
  
  // 全部消して以下一行に編集
  <h1>{{title}}</h1>

こんな感じで表示が変わる

.. figure:: /ex/angular/change-title.png

.. tip:: {{変数名}} でバインディングの構文となっている。tsファイルのtitleをHTMLの{{title}}に渡すことで表示される。


アプリスタイルの変更
--------------------------------------------
チュートリアルに従って、src/style.cssを修正

.. code-block:: css
  :caption: src/styles.css (excerpt)
  :linenos:
  
  /* Application-wide Styles */
  h1 {
    color: #369;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 250%;
  }
  h2,
  h3 {
    color: #444;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: lighter;
  }
  body {
    margin: 2em;
  }
  body,
  input[type="text"],
  button {
    color: #333;
    font-family: Cambria, Gergia;
  }
  /* everywhere else */
  * {
    font-family: Arial, Helvetica, sans-serif;
  }

文字の雰囲気が変わってればOK。こんな感じ。

.. figure:: /ex/angular/change-css.png

ヒーロー表示
============================================
heroesコンポーネント作成
--------------------------------------------

新規コンポーネント作成::

  $ ng generate component heroes
  CREATE src/app/heroes/heroes.component.html (21 bytes)
  CREATE src/app/heroes/heroes.component.spec.ts (626 bytes)
  CREATE src/app/heroes/heroes.component.ts (275 bytes)
  CREATE src/app/heroes/heroes.component.css (0 bytes)
  UPDATE src/app/app.module.ts (396 bytes)

.. figure:: /ex/angular/generate-component-heroes.png

HeroesComponentビューの表示
--------------------------------------------

.. code-block:: typescript
  :caption: app/heroes/heroes.component.ts
  :linenos:
  :emphasize-lines: 4-6, 9

  import { Component, OnInit } from '@angular/core';

  @Component({
    selector: 'app-heroes',
    templateUrl: './heroes.component.html',
    styleUrls: ['./heroes.component.css']
  })
  export class HeroesComponent implements OnInit {
    hero = 'Windstorm'; // 追加
    constructor() { }
    ngOnInit(): void {
    }

  }

.. tip:: 

  :selector: コンポーネントのCSS要素セレクター＝識別するHTML要素
  :templateUrl: コンポーネントのテンプレートファイルの場所
  :styleUrls: コンポーネントのプライベートCSSスタイルの場所

.. code-block:: html
  :caption: heroes.component.html
  :linenos:
  
  {{hero}}


.. code-block:: html
  :caption: src/app/app.component.html
  :linenos:
  :emphasize-lines: 2
  
  <h1>{{title}}</h1>
  <app-heroes></app-heroes>

ここまで対応すると、下記のように「Windstorm」が画面に表示されます。

.. figure:: /ex/angular/view-Windstorm.png


Heroインターフェースの作成
--------------------------------------------
ヒーローとして表示したいのは名前だけではない。インターフェースを作って表示する。

.. code-block:: typescript
  :caption: src/app/hero.ts(新規）
  :linenos:
  
  export interface Hero {
    id: number;
    name: string;
  }

.. code-block:: typescript
  :caption: app/heroes/heroes.component.ts
  :linenos:
  :emphasize-lines: 2, 10-13

  import { Component, OnInit } from '@angular/core';
  import { Hero } from '../hero';
  
  @Component({
    selector: 'app-heroes',
    templateUrl: './heroes.component.html',
    styleUrls: ['./heroes.component.css']
  })
  export class HeroesComponent implements OnInit {
    hero: Hero = {
      id: 1,
      name: 'Windstorm'
    };
    constructor() { }
    ngOnInit(): void {
    }

  }

.. code-block:: html
  :caption: app.component.html (template)
  :linenos:
  
  <h2>{{hero.name}} Details</h2>
  <div><span>id: </span>{{hero.id}}</div>
  <div><span>name: </span>{{hero.name}}</div>

表示はこんな感じ。

.. figure:: /ex/angular/view-id-Windstorm.png

UppercasePipeでの書式設定
--------------------------------------------

hero.nameのバインディングを修正::
  
  <h2>{{hero.name | uppercase}} Details</h2>

.. figure:: /ex/angular/view-id-Windstorm-upper.png

   

ヒーローの編集
--------------------------------------------
双方向バインディングできるように修正する。


.. code-block:: html
  :caption: app.component.html (template)
  :linenos:
  
  <h2>{{hero.name | uppercase}} Details</h2>
  <div><span>id: </span>{{hero.id}}</div>
  <div>
    <label>name:
      <input [(ngModel)]="hero.name" placeholder="name"/>
    </label>
  </div>

.. figure:: /ex/angular/ngModel.png


AppModule
--------------------------------------------
この状態では、以下のエラーが発生

.. figure:: /ex/angular/serve-error.png

.. tip:: [(ngModel)]が双方向バインディング構文。ngModelは有効なAngularディレクティブですが、デフォルトでは使用不可。FormsModuleモジュールをimportする必要あり。

.. code-block:: typescript
  :caption: src/app/app.module.ts
  :linenos:
  :emphasize-lines: 3,6,12,16
  
  import { BrowserModule } from '@angular/platform-browser';
  import { NgModule } from '@angular/core';
  import { FormsModule } from '@angular/forms'; // 追加

  import { AppComponent } from './app.component';
  import { HeroesComponent } from './heroes/heroes.component'; // 自動で追加されてた


  @NgModule({
    declarations: [
      AppComponent,
      HeroesComponent
    ],
    imports: [
      BrowserModule,
      FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
  })
  export class AppModule { }

.. tip:: moduleは、app.module.tsで一元管理。HeroesComponent は、generateの際に自動で追加された。

moduleを整備すれば、エラーは消えて動作するようになる。formを修正するとh2タグも同期して編集される。

.. figure:: /ex/angular/ngModel-fix.png

   

リスト
============================================
モック作成
--------------------------------------------

.. code-block:: typescript
  :caption: src/app/mock-heroes.ts
  :linenos:
  
  import { Hero } from './hero'

  export const HEROES: Hero[] = [
    { id: 11, name: 'Dr Nice' },
    { id: 12, name: 'Narco' },
    { id: 13, name: 'Bombasto' },
    { id: 14, name: 'Celeritas' },
    { id: 15, name: 'Magneta' },
    { id: 16, name: 'RubberMan' },
    { id: 17, name: 'Dynama' },
    { id: 18, name: 'Dr IQ' },
    { id: 19, name: 'Magma' },
    { id: 20, name: 'Tornado' }
  ];

ngForで表示
--------------------------------------------

.. code-block:: typescript
  :caption: app/heroes/heroes.component.ts
  :linenos:
  :emphasize-lines: 2, 10

  import { Component, OnInit } from '@angular/core';
  import { HEROES } from '../mock-heroes';

  @Component({
    selector: 'app-heroes',
    templateUrl: './heroes.component.html',
    styleUrls: ['./heroes.component.css']
  })
  export class HeroesComponent implements OnInit {
    heroes = HEROES;

    constructor() { }

    ngOnInit(): void {
    }

  }

.. code-block:: html
  :caption: app.component.html (template)
  :linenos:
  :emphasize-lines: 3
  
  <h2>My Heroes</h2>
  <ul class="heroes">
    <li *ngFor="let hero of heroes">
      <span class="badge">{{hero.id}}</span> {{hero.name}}
    </li>
  </ul>

.. tip::

  * ngForは、繰返しディレクティブ（ngForの前のアスタリスク(*)を忘れないように）
  * <li> を繰り返す
  * heroes（複数形） は HeroesComponentのリスト
  * hero（単数形） はループごとのオブジェクト

表示はこんな感じ。

.. figure:: /ex/angular/Mock-lists.png


hero個別のCSS整備
--------------------------------------------

.. code-block:: css
  :caption: src/app/heroes/heroes.component.css
  :linenos:
  :emphasize-lines: 8,18

  /* HeroesComponent's private CSS styles */
  .heroes {
    margin: 0 0 2em 0;
    list-style-type: none;
    padding: 0;
    width: 15em;
  }
  .heroes li {
    cursor: pointer;
    position: relative;
    left: 0;
    background-color: #EEE;
    margin: .5em;
    padding: .3em 0;
    height: 1.6em;
    border-radius: 4px;
  }
  .heroes li:hover {
    color: #607D8B;
    background-color: #DDD;
    left: .1em;
  }
  .heroes li.selected {
    background-color: #CFD8DC;
    color: white;
  }
  .heroes li.selected:hover {
    background-color: #BBD8DC;
    color: white;
  }
  .heroes .badge {
    display: inline-block;
    font-size: small;
    color: white;
    padding: 0.8em 0.7em 0 0.7em;
    background-color:#405061;
    line-height: 1em;
    position: relative;
    left: -1px;
    top: -4px;
    height: 1.8em;
    margin-right: .8em;
    border-radius: 4px 0 0 4px;
  }

.. figure:: /ex/angular/Mock-lists-css.png


クリックイベント
--------------------------------------------

クリックイベントのバインディング追加::

  <li *ngFor="let hero of heroes" (click)="onSelect(hero)">

componentを修正

.. code-block:: typescript
  :caption: app/heroes/heroes.component.ts
  :linenos:
  :emphasize-lines: 12, 19-21

  import { Component, OnInit } from '@angular/core';
  import { Hero } from '../hero';
  import { HEROES } from '../mock-heroes';

  @Component({
    selector: 'app-heroes',
    templateUrl: './heroes.component.html',
    styleUrls: ['./heroes.component.css']
  })
  export class HeroesComponent implements OnInit {
    heroes = HEROES;
    selectedHero: Hero;

    constructor() { }

    ngOnInit(): void {
    }

    onSelect(hero: Hero): void{
      this.selectedHero = hero;
    }
  }


ngIfで分岐を追加
--------------------------------------------
この時点で、ブラウザコンソールで以下のようなエラーが出てるはず。

.. figure:: /ex/angular/selectedHero-undefined.png


.. code-block:: html
  :caption: src/app/heroes/heroes.component.html (*ngIf)
  :linenos:
  :emphasize-lines: 1

  <h2>My Heroes</h2>
  <ul class="heroes">
    <li *ngFor="let hero of heroes"
      [class.selected]="hero === selectedHero"
      (click)="onSelect(hero)">
      <span class="badge">{{hero.id}}</span> {{hero.name}}
    </li>
  </ul>

  <div *ngIf="selectedHero">

    <h2>{{selectedHero.name | uppercase}} Details</h2>
    <div><span>id: </span>{{selectedHero.id}}</div>
    <div>
      <label>name:
        <input [(ngModel)]="selectedHero.name" placeholder="name"/>
      </label>
    </div>

  </div>

これで、初期状態でformがなく、選択するとformが表示されるようになる。

.. figure:: /ex/angular/if-selected.png

.. todo:: 以降次回予定

コンポーネント
============================================

サービス
============================================
ナビゲーション
============================================
サーバ通信
============================================
