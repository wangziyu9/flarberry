#include "TaskScheduler.h" //包含此头文件，才能使用调度器
#include "Adafruit_Sensor.h"
#include "DHT.h"           //加载DHT11的库
#define DHTTYPE DHT11      // 定义传感器类似 DHT11
#define DHTPIN 12          //宏定义DHT数据接口，编译时DHTPIN会替换成2

DHT dht(DHTPIN, DHTTYPE); //声明 dht 函数
const int pinD = 12;

int sensorPin = A1;  // select the input pin for the potentiometer
int sensorValue = 0; // variable to store the value coming from the sensor
const float R = 1000.0;

void setup()
{
    // 第12、13脚接有 LED
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);

    Sch.init(); //初始化调度器

    //向调度器中添加任务
    //第一个参数为要添加任务的函数名
    //第二个参数为任务第一次执行的时间，
    //    合理设置有利于防止任务重叠，有利以提高任务执行的精度
    //第三个参数是任务执行的周期
    //第二、三个参数的单位均为毫秒，也可配置定时器修改其单位
    //第四个参数代表任务是合作式还是抢占式
    //    一般取1就可以，更多用法请参考下文
    Sch.addTask(h_t_senser, 0, 1000, 1); //从第 0 毫秒开始闪烁 LED，每隔 1s, LED 状态改变一次
    Sch.addTask(eh_serser, 20, 500, 1);  //从第 20 毫秒开始闪烁 LED，每隔 0.5s, LED 状态改变一次

    Sch.start(); //启动调度器

    Serial.begin(9600);
    dht.begin(); //启动传感器
}

void loop()
{
    Sch.dispatchTasks(); // 执行被调度的任务，用调度器时放上这一句即可
}

// 把要调度的任务函数放下面

// 闪烁第 13 脚的 LED
void h_t_senser()
{
    delay(25000);                     //采样延时，每次抓取数据时间间隔 1~2秒钟
    float h = dht.readHumidity();    //读取湿度
    float t = dht.readTemperature(); //读取摄氏度
    if (isnan(h) || isnan(t))
    {
        Serial.println("Failed to read from DHT sensor!");
        return;
    } //检查抓取是否成功

    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print(" Temperature: ");
    Serial.print(t);
    Serial.println(" *C ");
}

// 闪烁第 12 脚的 LED
void eh_serser()
{
    sensorValue = analogRead(sensorPin);
    Serial.print("Earth_humidity ");
    float r = (sensorValue * R) / (1023 - sensorValue);
    Serial.print(r);
    Serial.println(" r");
    delay(25000);
}
