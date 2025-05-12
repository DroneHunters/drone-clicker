const config = {
    type: Phaser.AUTO,
    parent: 'game',
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

let game = new Phaser.Game(config);
let drone, partsText, parts = 0;

function preload() {
    this.load.image('drone', 'assets/drone.png');
    this.load.image('part', 'assets/part.png');
}

function create() {
    // Дрон
    drone = this.add.sprite(400, 300, 'drone').setInteractive();
    drone.on('pointerdown', () => {
        parts++;
        partsText.setText(`Детали: ${parts}`);
        this.add.sprite(Phaser.Math.Between(100, 700), 100, 'part');
    });

    // Текст
    partsText = this.add.text(20, 20, 'Детали: 0', { font: '24px Arial', fill: '#fff' });
}