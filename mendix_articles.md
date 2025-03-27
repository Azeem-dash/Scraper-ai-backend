# ARTICLE 1: Mendix Studio Pro 8 Beta: Make it native!
[Read More](https://www.mendix.com/blog/mendix-studio-pro-8-beta-make-it-native/)
--------------------------------------------------

![](https://play.vidyard.com/mL1gNHCUWCnpzz9wTtvLxT.jpg)

The Mendix 8 announcements at Mendix World 2019 made a huge impact, as we can tell from the many positive responses we received from our customers, partners, and colleagues. Today, I am very excited to announce the public beta release of Mendix Studio Pro 8!

The Mendix 8 release marks the first of multiple announcements that will put new features in your hands. There’s Mendix Studio Pro (formerly known as the Desktop Modeler), the world’s most sophisticated [low-code development environment](https://www.mendix.com/low-code-guide/) that gives developers control while being highly extensible. In addition, Mendix Studio (formerly known as the Web Modeler) now sees the light of day. As the world’s most powerful no-code development environment, Mendix Studio lets people in the business easily build their first-ever app. We’ll have more on Mendix Studio in a later blog post!

Today, I will cover how with low-code, Mendix Studio Pro 8 lets you build truly native mobile apps that have a consumer-grade experience. This is not just a feature, but an important new capability. Traditionally, native mobile development is very complex and expensive, but we are making it accessible through a low-code approach. And that’s for multiple platforms from a single model.

We’re also the first to do this.

**Why native mobile?**
----------------------

In the last few years, we’ve seen expectations regarding user experience increase, mobile devices become more powerful, and mobile become a dominant channel. For example, when it comes to banking, many users use a mobile app instead of a website, due to ease of use and options to pay with just a fingerprint. User experience is critical when building apps for consumers, as poor UX can lead to brand damage, decreased conversion, and users switching to competitors.

Great user experience is not only important for consumer apps. We also see a lot of use cases for business-to-business apps where the UX is critical and new (innovative) business models are made possible via native mobile technology. Think about a company that sells boilers and is dependent on other companies that install and maintain them. This company can provide mechanics with a great native app that connects with the boilers (for quick installation and inspection), and that can be used to order new parts or sell new boilers. By making the mechanics more efficient, brand adoption can increase, which leads to increased sales.

Native mobile is also of great value in business-to-employee scenarios, as it can make employees more efficient. This all goes hand-in-hand with leveraging native-device capabilities, the option to communicate with other devices and things, and performing tasks without a connection. Imagine a field service engineer who needs to do inspections at remote locations in factories where there is either no connection or no connection allowed. An offline-capable app that can connect to machines, read sensor data, and provide instructions for what to do allows the engineer to be much more efficient and less error-prone without any connection.

Native mobile is the way forward to give your customers and employees the experience they want and deserve.

**The next generation in mobile app development**
-------------------------------------------------

To build the next generation of mobile apps, we at Mendix consider the aspects below very important.

1. **Top-notch user experience using truly native technology**

![UX and native technology](https://www.mendix.com/wp-content/uploads/Image-1_truly-native.jpeg)Using native mobile technology, developers can build truly native apps that behave how users expect in terms of performance, snappiness, navigation, and gestures (like swiping to go back). This is accompanied with leveraging the powerful capabilities that devices offer nowadays, such as biometric authentication, camera functionality, Bluetooth, and newer technologies like augmented reality. Only with native technology can you get that high degree of user experience and leverage all of those device capabilities.

**2. Reliable & fast through an offline-first approach**

### 

A great user experience is not only achieved with native technology. It is very important that the user can always perform their tasks, even when there is little to no connection (which happens more than you think). Imagine you had a car accident and cannot use your insurer app, or an engineer needs to inspect a location but cannot do that because there is no connection. There are many more examples where not having a connection leads to poor user experience.

It’s important to remember that when the user is constantly relying on a connection and that connection is slow, the app will also behave slowly. This, again, leads to poor user experience.

We see a strong demand for building apps that always work, regardless of the connection state. That is why we adopted an offline-first approach. This does not rely on a connection, but a connection can be used when it exists. For more information on offline-first, keep reading.

**3. Great & powerful developer experiences**

Building great apps is one thing, but developers should also have a great experience while building these apps.

![powerful developer experience](https://www.mendix.com/wp-content/uploads/Image-3_user-experience.jpeg)That is why we added native mobile-focused features that enable you to quickly build beautiful apps and make it easy to leverage powerful device capabilities.

What is more, native technology helps improve the developer experience compared to using hybrid/web technology. That’s because developers do not need to spend time mimicking native behavior or dealing with web technology-related mobile issues.

**4. State-of-the-art & future-proof technology: React Native**

![React Native and Studio Pro](https://www.mendix.com/wp-content/uploads/Image-4_React-Native.jpeg)For the underlying technology we use [React Native](https://facebook.github.io/react-native/), a widely adopted and very popular open-source framework started by Facebook. There are some great showcases of apps built using React Native, and we are using this same technology!

For more great showcases, see [Who’s using React Native?](https://facebook.github.io/react-native/showcase).

Another great thing about React Native is that it has a large developer community building components for great visualizations and building components that leverage device capabilities that can be easily integrated into your Mendix apps. Because of this large community and the wide adoption of React Native, these are high-quality components that are actively maintained.

![Who is using React Native logos](https://www.mendix.com/wp-content/uploads/Image-5_React-users.png)

**How does it work?**
---------------------

To make this all possible, we added several new features and capabilities to the platform that enable you to build great [native mobile apps](https://www.mendix.com/blog/mobile-apps-go-native-part-ii-now-with-low-code/).

### New native navigation profile

A strength of Mendix is that you can expose functionality through different channels from a single app by using navigation profiles. Native mobile has been added as a new navigation profile, which means you can add a native mobile app next to your existing channels (for example, web and hybrid apps).

### Similar developer experience

You can build Mendix native mobile apps the same way you build web and hybrid mobile apps. You can use all the familiar Mendix components — like pages, widgets, nanoflows, JavaScript actions, and microflows — to build your native app.

However, there are some differences between building native apps and building hybrid apps. For example, the set of widgets (and their available properties) is slightly different, in order to optimize for mobile use. To be more specific, you can now select a pull-down action on a list view to do a refresh.

![Edit list view in Mendix 8](https://www.mendix.com/wp-content/uploads/Image-6_Pull-down-list.png)

An example of native-specific properties like pull down and scroll direction.

We value collaboration highly at Mendix, so each Mendix native mobile app comes with a feedback widget that allows users to give feedback on the app.

![Mendix native mobile app feedback widget](https://www.mendix.com/wp-content/uploads/Image-7_Feedback.png)

Another exciting new feature is that you can fully model the login process for your app. This empowers developers to create a great authentication experience. To make this easy, a standard login page and biometric authentication are available out of the box.

To summarize, you don’t need to be a mobile whiz kid to build great mobile apps. Your existing Mendix knowledge is enough.

### Make It Native app

You can quickly preview & test your mobile apps on a device using the Make It Native mobile app (available for [Android](https://play.google.com/store/apps/details?id=com.mendix.developerapp) and [iOS](https://docs.mendix.com/howto/mobile/getting-started-with-native-mobile#downloading-for-ios)). When you make a change to your app, hit the play button and the app will be automatically reloaded, making your changes visible while keeping the original state so that you are still on the same page with the same data. This creates a very short feedback cycle. Next to this, you can use a simple three-finger tab to reload the app, for example, after you make changes to the styling.

### Native Mobile Quickstart app

We released the [Native Mobile Quickstart](https://appstore.home.mendix.com/link/app/109511/) app in the Mendix App Store as a starter app that enables you to quickly build a native mobile app. It is ready to run out of the box, and it contains all the native widgets and actions that leverage device capabilities.

### Theming & styling

Atlas UI now contains a beautiful out-of-the-box theme for native mobile. This is a complete theme with styles and variations for all widgets in addition to page templates. Even more page templates will be added in the future.

![out-of-the-box themes for native mobile Mendix 8](https://www.mendix.com/wp-content/uploads/Image-8_Theming.png)

Mendix widgets include design properties that allow you to easily configure common styling options (that affect the appearance of the widget) in addition to many other useful options (like the spacing around the widget).

![Edit Action Button in Mendix 8](https://www.mendix.com/wp-content/uploads/Image-9_Edit-Action-Button.png)

Theming and styling are based on JavaScript instead of SASS/CSS, and they are optimized for mobile use cases. The days of having to apply CSS tricks for good UX are over with this mobile-optimized styling! It’s good to know that this is similar to CSS, but there are also quite a few differences. For more information, see [Native Styling](https://docs.mendix.com/refguide/native-styling-refguide) and [How to Create & Test a Native Mobile App](https://docs.mendix.com/howto/mobile/getting-started-with-native-mobile) in the Mendix documentation.

Because the styling is based on JavaScript, JavaScript functions and variables can be used, which can be very powerful. You can flip a single variable and get a dark theme. How cool is that?

![Feedback widget with dark mode theme](https://www.mendix.com/wp-content/uploads/Image-10_Dark-mode.png)

### New nanoflow actions

With this release, we added 50+ new nanoflow activities! We included these in the Native Mobile Quickstart app, but you can also download them via two modules in the Mendix App Store.

The [Native Mobile Resources](https://appstore.home.mendix.com/link/app/109513/) module contains native mobile-related nanoflow activities that leverage native device capabilities like the camera, location, fingerprint, and storage in addition to other device features like navigation, sharing data, showing notifications, and more.

Besides the Native Mobile Resources, there is the [NanoflowCommons](https://appstore.home.mendix.com/link/app/109515/) module, which contains more generic actions that can not only be used for native apps, but also for web and hybrid apps.

Finally, we added the following nanoflow actions directly to Studio Pro: List operations, List aggregation, and Show message.

![Mendix 8 nanoflow activities](https://www.mendix.com/wp-content/uploads/Image-11_Nanoflow-activity-examples.png)

Examples of native nanoflow activities

### JavaScript actions with an integrated editor

Another great feature in Mendix 8 is that it is now possible to build your own nanoflow actions using JavaScript. These pluggable nanoflow actions — called JavaScript actions in Studio Pro — can be used to leverage device capabilities or perform any type of logic. JavaScript actions should already be quite familiar to Mendix developers, because they are similar to Java actions. And you will find the most-loved features of Java actions available: different parameter types, exposing as a nanoflow activity in the Studio Pro Toolbox, and packaging and distributing through the public or private Mendix App Store.

What really makes JavaScript actions stand out is that you can edit them without leaving Mendix Studio Pro. There is a powerful editor integrated right inside the Code tab of the JavaScript action document. This is based on the [Monaco Editor](https://microsoft.github.io/monaco-editor/index.html), which is the editor that powers the most popular IDE, [Visual Studio Code](https://code.visualstudio.com/). This editor delivers a great experience, as it supports smart context-aware auto-completion, embedded documentation on web and Mendix APIs, correct indenting, and code-friendly shortcuts.

![Mendix Studio Pro JavaScript Editor](https://www.mendix.com/wp-content/uploads/Image-12_JavaScript-Editor.gif)

JavaScript actions open up a world of new possibilities and improve the developer experience, as there is better separation between UI components and actions. For more details on building your own JavaScript action, see [How to Write JavaScript Actions](https://docs.mendix.com/howto/extensibility/write-javascript-actions).

**Native widgets**
------------------

With this release, we included a great set of widgets so you can start making rich apps right out of the box. There are many core widgets available, like text, input types, buttons, lists, containers, and tab containers. And now there is a maps widget, progress bar, progress circle, slider, floating action button, badge, loading indicator, and web view. Note that these widgets are optimized for mobile. For example, the inputs use native controls and the appropriate keyboard type, the tabs animate nicely, and swiping works smoothly.

Here you can see examples of the widgets with some variations:

![Mendix 8 map widget example](https://www.mendix.com/wp-content/uploads/Image-13_Native-Widget-map.png)

![Mendix 8 data widget example](https://www.mendix.com/wp-content/uploads/Image-14_Native-Widget-data.png)

You can find all these widgets in the Native Mobile Quickstart app or download them separately in the Native Mobile Resources module from the Mendix App Store.

### Building your own widgets

Besides all of the widgets available out of the box, we made it easier to build your own widgets. These are called pluggable widgets, and they use modern and popular technologies. Building a widget for native mobile is basically the same as building a React (Native) component, so existing JavaScript development skills can easily be leveraged.

To support you even more, we released a Yeoman generator that can be used to easily generate a widget project. This will get you up and running quickly and creates a fast and easy developer flow for you. You can use this generator to create widgets for native mobile apps as well as for web and hybrid apps, based on JavaScript or TypeScript. The generator includes various options, such as creating an empty project based on a template and generating test cases.

There are a lot of open source React Native components available for you to easily integrate, as another powerful capability is the option to use external dependencies and install them via [npm](https://www.npmjs.com/).

If you want to build your own pluggable widget after reading this, check out our [Build Pluggable Widget](https://docs.mendix.com/howto/extensibility/pluggable-widgets) how-to docs.

### Offline-first

As mentioned above, it is important to have an offline-first approach in giving users a great experience and a reliable app. Mendix 8 contains some new features that make it easier than ever to do this.

By default, Mendix automatically analyzes your app’s data model to determine which entities should be synchronized based on the pages and nanoflows used within your offline navigation profile. In this release, we added configurable synchronization to optimize the default synchronization configuration. It is possible to limit what is downloaded by using XPath constraints. Furthermore, it is possible to disable downloads for an entity, which can be very useful in cases where objects should only be uploaded (for example, a “feedback” entity). This configuration can be found in your navigation profile.

![Customization offline synchronization](https://www.mendix.com/wp-content/uploads/Image-15_Offline-Sync.png)

We added some other useful features to make building offline-first apps easier: support for XPath expressions in the retrieve activity in nanoflows, the option to use a nanoflow as data source for a data view, and support for the nanoflow activities List operations, List aggregation, and Show message.

For more information on how our offline-first functionality works, see [Offline-First](https://docs.mendix.com/refguide/offline-first) in the Mendix documentation.

**What’s Next**
---------------

During the beta period, we will actively work with customers and partners to gather feedback, which we will use to improve the product. Here are some of the topics we will be working on for upcoming releases:

* App store publishing that makes it possible to build the binaries (APK & IPA) based on settings like your app ID, name, icon, and splash screen
* Sub-nanoflows, meaning, reusing nanoflows inside other nanoflows
* Calling a microflow from nanoflow, which is a big feature for offline apps that allows you to call microflows on the server to perform logic on the server or synchronize data
* More native page templates, widgets, features, and flexibility in layouts like the hamburger menu

Support for snippets and building blocks

**What if I already have a hybrid mobile app?**
-----------------------------------------------

As mentioned above, native mobile is available as a new channel (via a navigation profile), which can be added next to the hybrid profiles. This allows you to build a native mobile app right next to your hybrid mobile app from a single model.

You can reuse various parts of your hybrid apps in your native mobile apps, such as the domain model, nanoflows, microflows, and integrations. Pages for native mobile have a different layout, which allows you to convert a page to a native page by changing the layout. However, as native pages have a different set of widgets and properties, you will get consistency errors that you’ll need to solve.

The styling has to be created specifically for native mobile apps, as it’s based on JavaScript and is optimized for mobile use. You will probably want to do that anyway, in order to provide that excellent user experience.

For new apps, we recommend utilizing these native mobile features. However, whether you should migrate your hybrid mobile app to a native app or not is a decision you need to base on your specific situation and business case. During the beta period, you can get a first impression in order to see how and when you can start using native mobile.

**How can I get started?**
--------------------------

Can’t wait to get started? You can find a quick how-to [here](https://docs.mendix.com/howto/mobile/native-mobile) that guides you in building your first native mobile app in minutes. Soon, there will also be a training module, as part of the [Mendix Academy](https://gettingstarted.mendixcloud.com/).

Mendix Studio Pro 8.0.0 (beta) can be downloaded from the [Mendix App Store](https://appstore.home.mendix.com/link/modelers/) and you can find the release notes [here](https://docs.mendix.com/releasenotes/studio-pro/8.0). For more information about beta releases, see [What Are Mendix Beta Features?](https://docs.mendix.com/releasenotes/beta-features/).

**Go make it native!**
----------------------

You are all makers, and we can’t wait to see what the creative and innovative mobile apps you’re going to build! We would love to hear your feedback and hear more about the use-cases you have for Mendix native mobile apps. Feel free to contact me at [danny.roest@mendix.com](mailto:danny.roest@mendix.com). For product issues, please contact [Mendix Support](https://support.mendix.com/) or post your question on the Forum.

[![Unlock the full capabilities of Mendix 8. Leverage the new features to rapidly develop, iterate, and deploy applications. Try Mendix 8 now.](https://www.mendix.com/wp-content/uploads/Mendix8-CTA-blogbanner2.png)](https://appstore.home.mendix.com/link/modelers/)

![](https://www.mendix.com/wp-content/uploads/aws-cta.png)  

Drive Innovation with Mendix and AWS
------------------------------------

Leverage Mendix and 200+ AWS services to accelerate development and deliver unmatched value.

[Learn more](https://www.mendix.com/aws/)

==================================================

# ARTICLE 2: How to work with JavaScript and Mendix
[Read More](https://www.mendix.com/blog/how-to-work-with-javascript-and-mendix/)
--------------------------------------------------

Those familiar with superhero movies and other sci-fi genres, will be familiar with digital sidekicks hacking into security systems and more for the main protagonist of the story. But for my build, I would be focusing on the speech-to-text and text-to-speech aspects of my digital assistant voice app. I mean, how hard could that be after all? With little regard for my own sanity or stress levels, I dove head first into the abyss of speech synthesis technologies, and how to implement them in Javascript and Mendix.

#### “JavaScript is the only language that I’m aware of that people feel they don’t need to learn before they start using it.”

— Douglas Crockford

The Idea
--------

The design is simple — well as simple as I could make it. The idea is to create a Mendix app which can hear and understand a user’s spoken words and then respond through its own “voice”. Sounds easy right? Once I decided on a design, it was time to look for any existing technologies out there that I could use — not much point in redeveloping this from scratch when there are many voice platforms already out there, such IBM’s Watson and Google’s Cloud AI Platform.

However I’ve built chat bots before- at last year’s Mendix World, I hosted a Low Code live build with Jan de Vries. In the session I built out an Alexa skill which allowed a user to interact with a Mendix app, by speaking to Alexa. This time around I decided to focus less on the actual conversation and dialog, and more on the actual spoken word aspect of this build. If you would like to learn more about building conversation trees, I recommend you watch the recording from [Mendix World 2020](https://youtu.be/S53zYFINvtI).

The Design
----------

So what am I actually going to build? After some research I settled on a design, my app would focus on 2 core aspects:

1. A Speech-to-Text pluggable widget which will be able to hear and understand the user’s voice.
2. A Text-to-Speech JavaScript Action which will allow the app to respond out loud to the user.

For the widget I would be using a library I found on [Github](https://github.com/NikValdez/voiceTextTut/blob/master/src/App.js), which makes use of [Mozilla’s speech synthesis libraries.](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)

Conveniently for the JavaScript action I came across a [JavaScript tutorial created by Mendix](https://docs.mendix.com/howto/extensibility/write-javascript-actions) which does exactly this inside our own documentation.

Finally, in the Movies, the hero always has a cool name for their robotic side kick. In honour of this I decided to name my app **MAEVIS** which stands for “**Mendix’s Awesome Excellent Very Intelligent System**”

Building MAEVIS
---------------

Generally when building an app, I try to focus on the most challenging or complex processes first. As I already had a rough idea on how to get the app to speak, I decided to focus on building the widget which would allow MAEVIS to **hear me**. As I mentioned above I decided on using this [**Library**](https://github.com/NikValdez/voiceTextTut/blob/master/src/App.js) by [**NikValdez**](https://github.com/NikValdez) on Github.

I used the Mendix Widget generator to create my widget scaffold. I chose to build this using JavaScript ES6 and its built for web and hybrid mobile apps.

![](https://www.mendix.com/wp-content/uploads/0_EoAKICQR80GB6UVx.webp)

The main issue I ran into adapting this code to work in MAEVIS, was that the example uses a Functional component, and the widget scaffold generates the code as a Class component. Once I understood the issue it was simple to resolve it.

I ended up with this as the final widget code :

```
import React,{ Component, createElement, useState, useEffect } from "react";
```

```
import "./ui/SpeechToText.css";
```

```
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
```

```
const mic = new SpeechRecognition();
```

```
mic.continuous = true;
```

```
mic.interimResults = true;
```

```
mic.lang = 'en-US';
```

```
export default function SpeechToText(){
```

```
const [isListening, setIsListening] = useState(false);
```

```
const [note, setNote] = useState('');
```

```
const [savedNotes, setSavedNotes] = useState([]);
```

```
useEffect(() => {
```

```
handleListen()
```

```
}, [isListening]);
```

```
const handleListen = () => {
```

```
if (isListening) {
```

```
mic.start()
```

```
mic.onend = () => {
```

```
console.log('continue..')
```

```
mic.start()
```

```
}
```

```
} else {
```

```
mic.stop()
```

```
mic.onend = () => {
```

```
console.log('Stopped Mic on Click')
```

```
handleSaveNote()
```

```
}
```

```
}
```

```
mic.onstart = () => {
```

```
console.log('Mics on')
```

```
}
```

```
mic.onresult = event => {
```

```
const transcript = Array.from(event.results)
```

```
.map(result => result[0])
```

```
.map(result => result.transcript)
```

```
.join('')
```

```
console.log(transcript)
```

```
//textAttribute(transcript)
```

```
setNote(transcript)
```

```
mic.onerror = event => {
```

```
console.log(event.error)
```

```
}
```

```
}
```

```
}
```

```
const handleSaveNote = () => {
```

```
setSavedNotes([...savedNotes, note])
```

```
setNote('')
```

```
}
```

```
return  <span className="flexColumn">
```

```
<>
```

```
<p>{note}</p>
```

```
<button
```

```
className={isListening ? 'pulse-button btn-danger' : 'pulse-button'}
```

```
onClick={() => setIsListening(prevState => !prevState)}>
```

```
{isListening ? <span>🎙️Stop</span> : <span>🛑Start</span>}
```

```
</button>
```

```
</>
```

```
<>
```

```
<h2>Notes</h2>
```

```
{savedNotes.map(n => (
```

```
<p key={n}>{n}</p>
```

```
))}
```

```
</>
```

```
</span>;
```

```
}
```

I also added some styles to change to widgets front end, so it looks better than regular buttons on a screen :

```
.flexColumn{
```

```
display: inline-flex;
```

```
flex-direction: column;
```

```
}
```

```
.container {
```

```
width: 200px;
```

```
height: 100%;
```

```
margin: 0 auto 0;
```

```
perspective: 1000;
```

```
-webkit-perspective: 1000;
```

```
-webkit-backface-visibility: hidden;
```

```
backface-visibility: hidden;
```

```
background: #fff;
```

```
}
```

```
.pulse-button {
```

```
position: relative;
```

```
margin: auto;
```

```
display: block;
```

```
width: 10em;
```

```
height: 10em;
```

```
font-size: 1.3em;
```

```
font-weight: light;
```

```
font-family: 'Trebuchet MS', sans-serif;
```

```
text-transform: uppercase;
```

```
text-align: center;
```

```
line-height: 100px;
```

```
letter-spacing: -1px;
```

```
color: white;
```

```
border: none;
```

```
border-radius: 50%;
```

```
background: #5a99d4;
```

```
cursor: pointer;
```

```
box-shadow: 0 0 0 0 rgba(90, 153, 212, 0.5);
```

```
-webkit-animation: pulse 1.5s infinite;
```

```
animation: pulse 1.5s infinite;
```

```
}
```

```
.pulse-button:hover {
```

```
-webkit-animation: none;
```

```
animation: none;
```

```
}
```

```
@-webkit-keyframes pulse {
```

```
0% {
```

```
-moz-transform: scale(0.9);
```

```
-ms-transform: scale(0.9);
```

```
-webkit-transform: scale(0.9);
```

```
transform: scale(0.9);
```

```
}
```

```
70% {
```

```
-moz-transform: scale(1);
```

```
-ms-transform: scale(1);
```

```
-webkit-transform: scale(1);
```

```
transform: scale(1);
```

```
box-shadow: 0 0 0 50px rgba(90, 153, 212, 0);
```

```
}
```

```
100% {
```

```
-moz-transform: scale(0.9);
```

```
-ms-transform: scale(0.9);
```

```
-webkit-transform: scale(0.9);
```

```
transform: scale(0.9);
```

```
box-shadow: 0 0 0 0 rgba(90, 153, 212, 0);
```

```
}
```

```
}
```

```
@keyframes pulse {
```

```
0% {
```

```
-moz-transform: scale(0.9);
```

```
-ms-transform: scale(0.9);
```

```
-webkit-transform: scale(0.9);
```

```
transform: scale(0.9);
```

```
}
```

```
70% {
```

```
-moz-transform: scale(1);
```

```
-ms-transform: scale(1);
```

```
-webkit-transform: scale(1);
```

```
transform: scale(1);
```

```
box-shadow: 0 0 0 50px rgba(90, 153, 212, 0);
```

```
}
```

```
100% {
```

```
-moz-transform: scale(0.9);
```

```
-ms-transform: scale(0.9);
```

```
-webkit-transform: scale(0.9);
```

```
transform: scale(0.9);
```

```
box-shadow: 0 0 0 0 rgba(90, 153, 212, 0);
```

```
}
```

```
}
```

I must say, I consider getting this widget to render on screen one of my greatest development feats to date, and this is the first time in my life I truly felt that “AHA!” moment while coding in JavaScript. For those of wondering how long this took, it was about 3 days of pulling out my hair and yelling at my laptop, but in the end the pay-off for me was huge.

With the hard part done, it was an easy task to simply follow this [tutorial on building JavaScript actions](https://docs.mendix.com/howto/extensibility/write-javascript-actions).

In just an hour or two I had an action which could read out loud any text I gave it as a parameter. For those just looking for the code here it is, but I do recommend following this tutorial if you are new to JavaScript actions in Mendix.

```
// This file was generated by Mendix Studio Pro.
```

```
//
```

```
// WARNING: Only the following code will be retained when actions are regenerated:
```

```
// - the import list
```

```
// - the code between BEGIN USER CODE and END USER CODE
```

```
// - the code between BEGIN EXTRA CODE and END EXTRA CODE
```

```
// Other code you write will be lost the next time you deploy the project.
```

```
import { Big } from "big.js";
```

```
// BEGIN EXTRA CODE
```

```
// END EXTRA CODE
```

```
/**
```

```
* @param {string} text
```

```
* @returns {Promise.<boolean>}
```

```
*/
```

```
export async function JS_TextToSpeech(text) {
```

```
// BEGIN USER CODE
```

```
if (!text) {
```

```
return false;
```

```
}
```

```
if ("speechSynthesis" in window === false) {
```

```
throw new Error("Browser does not support text to speech");
```

```
}
```

```
// const utterance = new SpeechSynthesisUtterance(text);
```

```
// window.speechSynthesis.speak(utterance);
```

```
// return true;
```

```
return new Promise(function(resolve, reject) {
```

```
const utterance = new SpeechSynthesisUtterance(text);
```

```
utterance.onend = function() {
```

```
resolve(true);
```

```
};
```

```
utterance.onerror = function(event) {
```

```
reject("An error occured during playback: " + event.error);
```

```
};
```

```
window.speechSynthesis.speak(utterance);
```

```
});
```

```
// END USER CODE
```

```
}
```

Time to test it out
-------------------

So without further ado I would like to introduce you all to my creation [MAEVIS.](https://youtu.be/yb2nIXYMnpA)

Wrapping up
-----------

I want to emphasise just how much I learnt on this project, and although it was challenging I thoroughly recommend trying this out for yourself. I would’ve liked to add more to this build, but with some other really exciting projects in the works I have to leave it here.

Ideally I wanted the widget itself to trigger the Nanoflow which triggers the Text to Speech JavaScript action. And I think it would be great to utilise props to extract the dialogue from the widget back into Mendix, instead of simply storing it in the widget’s state. I will continue to work on these features and may post a follow up to this in the future, but until then I think its a great exercise for all of you to try do exactly this! Please reach out to me if you use this, I would love to see what crazy ideas this gives all of you. Until then, remember — Go Make it!

==================================================

# ARTICLE 4: Explained: Asynchronous vs. Synchronous Programming
[Read More](https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/)
--------------------------------------------------

Asynchronous and synchronous programming: What’s the difference?
----------------------------------------------------------------

Synchronous, sometimes called “sync,” and asynchronous, also known as “async,” are two different programming models.

Understanding how these two models differ is critical for:

* Building application programming interfaces (APIs)
* Creating event-based architectures
* Deciding how to handle long-running tasks

But before deciding which method to use and when, it’s important to know a few quick facts about synchronous and asynchronous programming.

### Programming asynchronous applications

Asynchronous programming is a multithreaded model that’s applied to networking and communications.

[Asynchronous is a non-blocking architecture](https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous#:~:text=does%20not%20block%20other%20processes%20while%20waiting%20for%20the%20response), which means it doesn’t block further execution while one or more operations are in progress. With async programming, multiple related operations can run concurrently without waiting for other tasks to complete. 

One way of programming asynchronous applications is with [low-code application development](https://www.mendix.com/low-code-guide/). Multiple developers can work on projects simultaneously in a low-code platform, which helps accelerate the process of building apps.

Another example is texting. Texting is an asynchronous communication method. One person can text, and the recipient can respond at leisure. In the meantime, the sender may do other things while waiting for a response.

> Think of **asynchronous** programming as adaptable, and **synchronous** programming as strict.

### Programming synchronous applications

Synchronous is a blocking architecture and is best for programming reactive systems.

As a single-thread model, it follows a strict set of sequences, which means that operations are performed one at a time, in perfect order.

While one operation is being performed, other operations’ instructions are blocked. The completion of the first task triggers the next, and so on.

To illustrate how synchronous programming works, think of a telephone conversation. While one person speaks, the other listens. When the first person finishes, the second tends to respond immediately.

### JavaScript

In the conversation about synchronous and asynchronous programming, there is a curveball called JavaScript.

JavaScript is a common scripting language that’s used to make websites interactive. JavaScript is an asynchronous and concurrent programming language that offers a lot of flexibility. It’s single-threaded like synchronous but also non-blocking like asynchronous.

Although it’s synchronous by nature, JavaScript benefits from an asynchronous process. [Long-running JavaScript](https://dotnettutorials.net/lesson/javascript-promise/) functions can make the user interface (UI) or server unresponsive until the function has returned, resulting in a less-than-stellar user experience.

However, there are some instances where users can benefit from blocking programming, for example, when making an online payment.

The benefit of JavaScript is that it offers the best of both worlds: Single-thread and multi-thread, blocking and non-blocking. With this flexibility, programmers can write code in a single programming language instead of two—one for synchronous operations and another for asynchronous operations.

### Related Content

[![Programming in a Low-Code World](https://www.mendix.com/wp-content/uploads/Blog-Thumbnail_Programming-in-a-Low-Code-World.png)

Further reading

Programming in a Low-Code World](https://www.mendix.com/blog/writing-code-in-a-low-code-world/)

Asynchronous vs. synchronous programming
----------------------------------------

Ultimately, the choice comes down to operational dependencies. Do you want the start of an operation to depend on another operation’s completion, or do you want it to run independently?

**Asynchronous** is a non-blocking architecture, so the execution of one task isn’t dependent on another. Tasks can run simultaneously.

**Synchronous** is a blocking architecture, so the execution of each operation depends on completing the one before it. Each task requires an answer before moving on to the next iteration.

The differences between asynchronous and synchronous include:

* **Async** is non-blocking, which means it will send multiple requests to a server.
* **Sync** is blocking — it will only send the server one request at a time and wait for that request to be answered by the server.
* **Async** increases throughput because multiple operations can run at the same time.
* **Sync** is slower and more methodical.

Both async and sync can be single-thread or multi-thread. The main difference is that an asynchronous system will not block a thread during an input/output operation.

![](https://www.mendix.com/wp-content/uploads/When-to-use-Async-vs-Sync-Programming.png)


> Differences aside, async and sync methods have advantages for different stakeholders: Async for users and sync for developers.

**Asynchronous** programming enhances the user experience by decreasing the lag time between when a function is called and when the value of that function is returned. Async programming translates to a faster, more seamless flow in the real world.

For example, users want their apps to run fast, but fetching data from an API takes time. In these cases, asynchronous programming helps the app screen load more quickly, improving the user experience.

**Synchronous** programming, on the other hand, is advantageous for developers. Synchronous programming is much easier to code. It’s well supported among all programming languages, and as the default programming method, developers don’t have to spend time learning something new that could open the door to bugs.

### Related Content

[![illustration of the human brain with connected nodes to show how AI models work.](https://www.mendix.com/wp-content/uploads/Blog_Different-AI-Models.png)

Further reading

What Are the Different Types of AI Models?](https://www.mendix.com/blog/what-are-the-different-types-of-ai-models/)

Async and sync use cases
------------------------

Programming makes our digital world run, but without the right pairing of programs and operations, chaos and poor user experiences would ensue. Our digital world could spin into a mad, hyperactive frenzy if operations inappropriately rely on asynchronous programming.

And if operations are inappropriately relying on synchronous programming, our digital world could come to a screeching halt. It’s imperative to understand when to use each type of programming.

### When to use async programming

Asynchronous programming is critical to programming independent tasks.

For instance, asynchronous programs are ideal for development projects with many iterations. Asynchronous programming will keep development moving forward because steps don’t have to follow a fixed sequence.

Responsive UI is a great use case for asynchronous planning. Take, for example, a shopping app. When a user pulls up their order, the font size should increase. Instead of first waiting to load the history and update the font size, asynchronous programming can make both actions happen simultaneously.

### When to use sync programming

Asynchronous programming is relatively complex. It can overcomplicate things and make code difficult to read. On the other hand, synchronous programming is fairly straightforward; its code is easier to write and doesn’t require tracking and measuring process flows (as async does).

Because tasks depend on each other, you have to know if they can run independently without interrupting each other.

Synchronous programming could also be appropriate for a [customer-facing shopping app](https://www.mendix.com/blog/customer-facing-applications/). Users want to buy all their items together rather than individually when checking out online. Instead of completing an order every time the user adds something to their cart, synchronous programming ensures that the payment method and shipping destination for all items are selected at the same time.

How to choose between asynchronous and synchronous programming
--------------------------------------------------------------

When deciding which approach to take, consider asynchronous programming adaptable and **synchronous** programming strict.

Asynchronous programming is the multitasker, moving from one to-do to the other and alerting the system when each task is complete. Synchronous programming functions with a one-track mind, checking off one task at a time in a rigid sequence.

* **Asynchronous programming allows more things to be done simultaneously** and is typically used to enhance the user experience by providing an effortless, quick-loading flow.
* **Synchronous programming is best utilized in reactive systems.** While it is simpler for developers to code and is recognized by every programming language, sync is resource-intensive and can slow things down.

![mendix logo](https://www.mendix.com/wp-content/uploads/mendix-ide-blog-cta-image.png)  

Turn Your Spreadsheet Into an App in Less Than 1 Minute
-------------------------------------------------------

Sign up now to simplify application development with the leader in low-code. Mendix is free to get started.

[Get started](https://signup.mendix.com/link/signup)

==================================================

# ARTICLE 5: A Mendix SDK Primer — Part 1
[Read More](https://www.mendix.com/blog/a-mendix-sdk-primer-part-1/)
--------------------------------------------------

In this short series, I shall illustrate how SDKs can be used to perform useful operations against an app. This first post is to get you started by **setting up a development environment** using NodeJS, creating a TypeScript script **to use the SDK** as well as executing that script.

I don’t intend this to be a TypeScript/JavaScript tutorial (I’m hardly in a good position to do that and there are lots of fine resources available online) and **I will focus on the aspects of the SDK** rather than the code details.

![](https://www.mendix.com/wp-content/uploads/1_dc-ybpOt-cRDIaJ9gppbwA.webp)

Why might you want to use the SDK?
----------------------------------

There are a large number of use cases that the Mendix Model SDK can support, to name just a few:

**The extraction of the details of all or part of an app model for translation into a different medium.**For example, you may wish to extract information from the model to produce your own documentation, or you might wish to extract the logic in microflows **to build equivalents in another language** such as JavaScript or C#.

**The automated updating of apps to enforce compliance with development or security standards.** For example, you might want to enforce common microflow/nanoflow naming standards or require that Entities have appropriate minimum access permissions applied.

**The automated creation of Code, Pages, Entities, etc. in an app from parameterized input.** For example, you may want to automate the process of copying the structure or schema of a data source and build that into a Mendix app.

Development Environment
-----------------------

Developers have their own preferences when it comes to tools. You will need NodeJS and a script editor as a minimum — I use Visual Studio Code for editing, available from [Visual Studio Code](https://code.visualstudio.com/), as I like its TypeScript support. I will not suggest any fancy setup and configuration for the environment but just keep things simple — a single folder to hold the scripts that I build.

There is a lot of documentation relating to the Platform and Model SDKs available on the docs page: [**Mendix Platform SDK**](https://docs.mendix.com/apidocs-mxsdk/mxsdk/ "https://docs.mendix.com/apidocs-mxsdk/mxsdk/").

NodeJS Installation
-------------------

Download and install the latest stable version of NodeJS which can be found at [NodeJS](https://nodejs.org/) with the English language download page at [NodeJS English Downloads](https://nodejs.org/en/download/releases/).

*If you have an earlier version of NodeJS already installed and wish to retain it then you can use a tool such as the NodeJS Version Manager ‘nvm’ which will allow you to install and manage multiple versions of NodeJS and switch between them. A selection of package managers is described at* [*NodeJS Package Managers*](https://nodejs.org/en/download/package-manager)*.*

Create a working folder and initialize it
-----------------------------------------

Next, I need somewhere to put my work so I create a folder to work in. Then I initialize that with the NodeJS package manager and ensure that the TypeScript package is installed.

```
mkdir SDKBlog
cd SDKBlog
npm init --yes
npm install -g typescript
```

Next switch over to your editor and create or edit a file in the folder called **package.json** and change that file to include dependencies for the SDK packages. It should look something like this:

```
{
    "name": "sdkblog",
    "version": "1.0.0",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
        "mendixmodelsdk": "^4.56.0",
        "mendixplatformsdk": "^5.0.0"
    },
    "devDependencies": {},
    "description": ""
}
```

**Download the SDK packages by using npm install**. This will create a sub-folder called ‘**node\_modules**’ where a hierarchy of various package files will be stored.

```
npm install
```

Finally, **create or edit a tsconfig.json** **file** to specify the compiler options and the name of the TypeScript file being created. Each time you add a new TypeScript file to the folder you can add it to the tsconfig.json file and then when you run the TypeScript compiler command ‘tsc’ it will compile all the files into JavaScript so that they can be executed.

```
{
    "compilerOptions" : {
        "module" : "commonjs",
        "target" : "es2020",
        "strict": true
    },
    "files" : [
        "showdocument.ts"
    ]
}
```

Get a Personal Access Token
---------------------------

You will need to go to the Mendix Warden site at [Mendix Warden](https://warden.mendix.com). Once there, you will need to log in with your Mendix Developer Portal credentials.

Create a Personal Access Token to access the repository functions, for example:

![](https://www.mendix.com/wp-content/uploads/1_PVMx1QIw2v8fxxDhM_R6iw.webp)

Save the generated token in an environment variable called **MENDIX\_TOKEN**. Instructions on how to do this are available on the [Mendix PAT Setup Page](https://docs.mendix.com/apidocs-mxsdk/mxsdk/setup-your-pat/#3-saving-the-personal-access-token-as-an-environment-variable).

Having completed this **you should now be ready to use the SDKs.**

App to JavaScript Script
------------------------

The script I’ll write here is a useful tool that you can use when you are doing any Mendix SDK work.

It will pull down the model from an existing Mendix app and find a document in the model that you specify and output the definition of that document as JavaScript code.

Believe me, when you start working with the Mendix SDK you will probably use this time and again as there is nothing better than eyeballing an existing example to enhance your understanding of how to use the SDK and the model of an app.

The script is on Github and the link to the Github project is at the end of this blog posting below.

Preliminaries
-------------

The script opens by expecting the command line to hold a project nickname (any name you want) and the qualified name of the Mendix document (microflow/form/enumeration) — so this will be just the module name if you want the domain model extracted, or the module name plus a period plus the document name. If you are accessing a different project for the first time you will need to add the app ID to the command line (taken from the General tab on the Mendix Developer portal page for the app), and a branch name if you don’t want to use the default branch.

```
import { JavaScriptSerializer } from "mendixmodelsdk";
import { MendixPlatformClient, OnlineWorkingCopy } from "mendixplatformsdk";
import * as fs from "fs";
```

```
// Usage: node showdocument.js nickname documentname appID branch
//   nickname is your own name for the app
//   documentname if the qualified name (module.document) of the document to serialize
//   appID is the appID for the app (taken from the Mendix developer portal page)
//   branch is the name of the branch to use
//
// The appID and branch are only needed when setting up a new working copy
//
// The appID, branch name and working copy ID are saved in a file called nickname.workingcopy in the
// current folder so they can be used next time if possible
//
const args = process.argv.slice(2);
```

```
main(args);
```

```
async function main(args: string[])
{
    var appID = "";
    var branch = "";
    var documentname = "";
```

```
    if (args.length < 1)
    {
        console.log(`Need at least a nickname and document name on the command line`);
        return;
    }
```

```
    const nickname = args[0].split(' ').join('');
    documentname = args[1];
    if (args.length > 2)
        appID = args[2];
    if (args.length > 3)
        branch = args[3];
```

```
    const workingCopyFile = nickname + '.workingcopy';
```

```
    var wcFile;
    var wcID;
```

```
    try
    {
        wcFile = fs.readFileSync(workingCopyFile).toString();
        appID = wcFile.split(':')[0];
        branch = wcFile.split(':')[1];
        wcID = wcFile.split(':')[2];
    }
    catch
    {
        wcFile = "";
        wcID = "";
```

```
        if (appID === "")
        {
            console.log("Need an appID on the command line if no workingcopy file is present for the nickname");
            return;
        }
    }
```

When the script is run, it will create a file named with the nickname you gave + ‘.workingcopy’, and in there it will store the app ID, the branch name, and the working copy id that is generated. This is so that, the next time you run the script for the same app (nickname) it will read in the working copy id you created last and use that again. This makes the process much faster.

```
    const client = new MendixPlatformClient();
    var workingCopy:OnlineWorkingCopy;
```

```
    const app = client.getApp(appID);
```

```
    var useBranch = branch;
```

```
    if (wcID != "")
    {
        try
        {
            console.log("Opening existing working copy");
            workingCopy = app.getOnlineWorkingCopy(wcID);
        }
        catch (e)
        {
            console.log(`Failed to get existing working copy ${wcID}: ${e}`);
            wcID = ""
        }
    }
```

```
    if (wcID === "")
    {
        const repository = app.getRepository();
```

```
        if ((branch === "") || (branch === "trunk") || (branch === "main"))
        {
            const repositoryInfo = await repository.getInfo();
            if (repositoryInfo.type === "svn")
                useBranch = "trunk";
            else
                useBranch = "main";
        }
```

```
        try
        {
            workingCopy = await app.createTemporaryWorkingCopy(useBranch);
            wcID = workingCopy.workingCopyId;
        }
        catch (e)
        {
            console.log(`Failed to create new working copy for app ${appID}, branch ${useBranch}: ${e}`);
            return;
        }
    }
```

```
    fs.writeFileSync(workingCopyFile, `${appID}:${useBranch}:${wcID}`);
```

Using the SDK
-------------

Having created/opened the working copy, the script now opens the model for the app, finds the domain model or the document specified, calls the JavaScript deserializer and writes the output to the console.

Note that the script assumes that a document name without a period character is a module name and you want the domain model for that module extracted. Otherwise, the supplied name is regarded as a qualified document name (module.document).

```
    const model = await workingCopy!.openModel();
```

```
    console.log(`Opening ${documentname}`);
```

```
    if (documentname.split(".").length <= 1)
    {
        const domainmodelinterfaces = model.allDomainModels().filter(dm => dm.containerAsModule.name === documentname);
        if (domainmodelinterfaces.length < 1)
            console.log(`Cannot find domain model for ${document}`);
        else
        {
            try
            {
                const domainmodelinterface = domainmodelinterfaces[0];
                const domainmodel = await domainmodelinterface.load();
                 console.log(JavaScriptSerializer.serializeToJs(domainmodel));
            }
            catch(e)
            {
                console.log(`Error occured: ${e}`);
            }
        }
    }
    else
    {
        const documentinterfaces = model.allDocuments().filter(doc => doc.qualifiedName === documentname);
        if (documentinterfaces.length < 1)
            console.log(`Cannot find document for ${document}`);
        else
        {
            try
            {
                const documentinterface = documentinterfaces[0];
                const document = await documentinterface.load();
                console.log(JavaScriptSerializer.serializeToJs(document));
            }
            catch(e)
            {
                console.log(`Error occured: ${e}`);
            }
        }
```

```
    }
```

```
}
```

Examples
--------

Before running the script, or after you have modified the script you should compile it from TypeScript into JavaScript using the command ‘tsc’. This will work provided you have the TypeScript file name included in the tsconfig.json as described earlier.

```
tsc
```

Otherwise, you can compile a specific TypeScript file using a command like:

```
tsc showdocument.ts
```

First, I pulled down the domain model of the Administration model using the following command. I chose ‘fred’ as my nickname for the app.

```
node showdocument.js fred Administration 8252db0e-6235-40a5-9502-36e324c618d7
```

The output can be very long so I shall just show a part of it.

```
    var generalization1 = domainmodels.Generalization.create(model);
    // Note: this is an unsupported internal property of the Model SDK which is subject to change.
     generalization1.__generalization.updateWithRawValue("System.User");
```

```
    var stringAttributeType1 = domainmodels.StringAttributeType.create(model);
```

```
    var storedValue1 = domainmodels.StoredValue.create(model);
```

```
    var fullName1 = domainmodels.Attribute.create(model);
    fullName1.name = "FullName";
    fullName1.type = stringAttributeType1;   // Note: for this property a default value is defined.
    fullName1.value = storedValue1;   // Note: for this property a default value is defined.
```

```
    var stringAttributeType2 = domainmodels.StringAttributeType.create(model);
```

```
    var storedValue2 = domainmodels.StoredValue.create(model);
```

```
    var email1 = domainmodels.Attribute.create(model);
    email1.name = "Email";
    email1.type = stringAttributeType2;   // Note: for this property a default value is defined.
    email1.value = storedValue2;   // Note: for this property a default value is defined.
```

```
    var booleanAttributeType1 = domainmodels.BooleanAttributeType.create(model);
```

```
    var storedValue3 = domainmodels.StoredValue.create(model);
    storedValue3.defaultValue = "true";
```

```
    var isLocalUser1 = domainmodels.Attribute.create(model);
    isLocalUser1.name = "IsLocalUser";
    isLocalUser1.type = booleanAttributeType1;   // Note: for this property a default value is defined.
    isLocalUser1.value = storedValue3;   // Note: for this property a default value is defined.
```

```
    var memberAccess1 = domainmodels.MemberAccess.create(model);
    memberAccess1.attribute = model.findAttributeByQualifiedName("Administration.Account.FullName");
    memberAccess1.accessRights = domainmodels.MemberAccessRights.ReadWrite;
```

```
    var memberAccess2 = domainmodels.MemberAccess.create(model);
    memberAccess2.attribute = model.findAttributeByQualifiedName("Administration.Account.Email");
    memberAccess2.accessRights = domainmodels.MemberAccessRights.ReadWrite;
```

```
    var memberAccess3 = domainmodels.MemberAccess.create(model);
    memberAccess3.attribute = model.findAttributeByQualifiedName("Administration.Account.IsLocalUser");
    memberAccess3.accessRights = domainmodels.MemberAccessRights.ReadOnly;
```

```
    var accessRule1 = domainmodels.AccessRule.create(model);
    accessRule1.memberAccesses.push(memberAccess1);
    accessRule1.memberAccesses.push(memberAccess2);
    accessRule1.memberAccesses.push(memberAccess3);
    accessRule1.moduleRoles.push(model.findModuleRoleByQualifiedName("Administration.Administrator"));
    accessRule1.allowCreate = true;
    accessRule1.allowDelete = true;
```

```
    var memberAccess4 = domainmodels.MemberAccess.create(model);
    memberAccess4.attribute = model.findAttributeByQualifiedName("Administration.Account.FullName");
    memberAccess4.accessRights = domainmodels.MemberAccessRights.ReadOnly;
```

```
    var memberAccess5 = domainmodels.MemberAccess.create(model);
    memberAccess5.attribute = model.findAttributeByQualifiedName("Administration.Account.Email");
    memberAccess5.accessRights = domainmodels.MemberAccessRights.ReadOnly;
```

```
    var memberAccess6 = domainmodels.MemberAccess.create(model);
    memberAccess6.attribute = model.findAttributeByQualifiedName("Administration.Account.IsLocalUser");
```

```
    var accessRule2 = domainmodels.AccessRule.create(model);
    accessRule2.memberAccesses.push(memberAccess4);
    accessRule2.memberAccesses.push(memberAccess5);
    accessRule2.memberAccesses.push(memberAccess6);
    accessRule2.moduleRoles.push(model.findModuleRoleByQualifiedName("Administration.User"));
    accessRule2.defaultMemberAccessRights = domainmodels.MemberAccessRights.ReadOnly;
```

```
    var memberAccess7 = domainmodels.MemberAccess.create(model);
    memberAccess7.attribute = model.findAttributeByQualifiedName("Administration.Account.FullName");
    memberAccess7.accessRights = domainmodels.MemberAccessRights.ReadWrite;
```

```
    var memberAccess8 = domainmodels.MemberAccess.create(model);
    memberAccess8.attribute = model.findAttributeByQualifiedName("Administration.Account.Email");
```

```
    var memberAccess9 = domainmodels.MemberAccess.create(model);
    memberAccess9.attribute = model.findAttributeByQualifiedName("Administration.Account.IsLocalUser");
```

```
    var accessRule3 = domainmodels.AccessRule.create(model);
    accessRule3.memberAccesses.push(memberAccess7);
    accessRule3.memberAccesses.push(memberAccess8);
    accessRule3.memberAccesses.push(memberAccess9);
    accessRule3.moduleRoles.push(model.findModuleRoleByQualifiedName("Administration.User"));
    accessRule3.xPathConstraint = "[id='[%CurrentUser%]']";
```

```
    var account1 = domainmodels.Entity.create(model);
    account1.name = "Account";
    account1.location = {"x":220,"y":140};
    account1.generalization = generalization1;   // Note: for this property a default value is defined.
    account1.attributes.push(fullName1);
    account1.attributes.push(email1);
    account1.attributes.push(isLocalUser1);
    account1.accessRules.push(accessRule1);
    account1.accessRules.push(accessRule2);
    account1.accessRules.push(accessRule3);
```

Then I pulled down the ChangeMyPassword microflow from the model by running the following command. Note that no app ID was needed as it could use the existing working copy that has just been created.

```
node showdocument.js fred Administration.ChangeMyPassword
```

This output is even longer so again I will just cut out part of the results.

```
    var expressionSplitCondition1 = microflows.ExpressionSplitCondition.create(model);
    expressionSplitCondition1.expression = "$AccountPasswordData/NewPassword = $AccountPasswordData/ConfirmPassword";
```

```
    var exclusiveSplit1 = microflows.ExclusiveSplit.create(model);
    exclusiveSplit1.relativeMiddlePoint = {"x":430,"y":200};
    exclusiveSplit1.size = {"width":130,"height":80};
    exclusiveSplit1.splitCondition = expressionSplitCondition1;   // Note: for this property a default value is defined.
    exclusiveSplit1.caption = "Passwords equal?";
```

```
    var translation1 = texts.Translation.create(model);
    translation1.languageCode = "en_US";
    translation1.text = "The new passwords do not match.";
```

```
    var translation2 = texts.Translation.create(model);
    translation2.languageCode = "nl_NL";
    translation2.text = "De nieuwe wachtwoorden komen niet overeen.";
```

```
    var text1 = texts.Text.create(model);
    text1.translations.push(translation1);
    text1.translations.push(translation2);
```

```
    var textTemplate1 = microflows.TextTemplate.create(model);
    textTemplate1.text = text1;   // Note: for this property a default value is defined.
```

```
    var showMessageAction1 = microflows.ShowMessageAction.create(model);
    showMessageAction1.template = textTemplate1;   // Note: for this property a default value is defined.
    showMessageAction1.type = microflows.ShowMessageType.Error;
```

```
    var actionActivity1 = microflows.ActionActivity.create(model);
    actionActivity1.relativeMiddlePoint = {"x":430,"y":75};
    actionActivity1.size = {"width":120,"height":60};
    actionActivity1.action = showMessageAction1;
```

```
    var endEvent1 = microflows.EndEvent.create(model);
    endEvent1.relativeMiddlePoint = {"x":430,"y":-20};
    endEvent1.size = {"width":20,"height":20};
```

```
    var startEvent1 = microflows.StartEvent.create(model);
    startEvent1.relativeMiddlePoint = {"x":-220,"y":200};
    startEvent1.size = {"width":20,"height":20};
```

```
    var closeFormAction1 = microflows.CloseFormAction.create(model);
```

```
    var actionActivity2 = microflows.ActionActivity.create(model);
    actionActivity2.relativeMiddlePoint = {"x":1110,"y":200};
    actionActivity2.size = {"width":120,"height":60};
    actionActivity2.action = closeFormAction1;
```

```
    var endEvent2 = microflows.EndEvent.create(model);
    endEvent2.relativeMiddlePoint = {"x":1230,"y":200};
    endEvent2.size = {"width":20,"height":20};
```

```
    var memberChange1 = microflows.MemberChange.create(model);
    // Note: this is an unsupported internal property of the Model SDK which is subject to change.
    memberChange1.__attribute.updateWithRawValue("System.User.Password");
    memberChange1.value = "$AccountPasswordData/NewPassword";
```

```
    var changeObjectAction1 = microflows.ChangeObjectAction.create(model);
    changeObjectAction1.items.push(memberChange1);
    changeObjectAction1.refreshInClient = true;
    changeObjectAction1.commit = microflows.CommitEnum.Yes;
    changeObjectAction1.changeVariableName = "Account";
```

```
    var actionActivity3 = microflows.ActionActivity.create(model);
    actionActivity3.relativeMiddlePoint = {"x":620,"y":200};
    actionActivity3.size = {"width":120,"height":60};
    actionActivity3.action = changeObjectAction1;
    actionActivity3.caption = "Save password";
    actionActivity3.autoGenerateCaption = false;
```

```
    var expressionSplitCondition2 = microflows.ExpressionSplitCondition.create(model);
    expressionSplitCondition2.expression = "$OldPasswordOkay";
```

```
    var exclusiveSplit2 = microflows.ExclusiveSplit.create(model);
    exclusiveSplit2.relativeMiddlePoint = {"x":230,"y":200};
    exclusiveSplit2.size = {"width":120,"height":80};
    exclusiveSplit2.splitCondition = expressionSplitCondition2;   // Note: for this property a default value is defined.
    exclusiveSplit2.caption = "Old password okay?";
```

```
    var endEvent3 = microflows.EndEvent.create(model);
    endEvent3.relativeMiddlePoint = {"x":230,"y":-20};
    endEvent3.size = {"width":20,"height":20};
```

```
    var basicCodeActionParameterValue1 = microflows.BasicCodeActionParameterValue.create(model);
    basicCodeActionParameterValue1.argument = "$Account/Name";
```

```
    var javaActionParameterMapping1 = microflows.JavaActionParameterMapping.create(model);
    // Note: this is an unsupported internal property of the Model SDK which is subject to change.
    javaActionParameterMapping1.__parameter.updateWithRawValue("System.VerifyPassword.userName");
    javaActionParameterMapping1.parameterValue = basicCodeActionParameterValue1;   // Note: for this property a default value is defined.
```

```
    var basicCodeActionParameterValue2 = microflows.BasicCodeActionParameterValue.create(model);
    basicCodeActionParameterValue2.argument = "$AccountPasswordData/OldPassword";
```

```
    var javaActionParameterMapping2 = microflows.JavaActionParameterMapping.create(model);
    // Note: this is an unsupported internal property of the Model SDK which is subject to change.
    javaActionParameterMapping2.__parameter.updateWithRawValue("System.VerifyPassword.password");
    javaActionParameterMapping2.parameterValue = basicCodeActionParameterValue2;   // Note: for this property a default value is defined.
```

OK, so these snippets show that the output can be rather extensive and it may hint at some of the complexity that can come from using the SDK, though if you are familiar with using JavaScript/TypeScript then you will probably feel much more comfortable.

Similar commands can be used to extract the definitions for the various document types within a Mendix app. The JavaScriptSerializer can provide you with code that might be used directly (or after modification) to update this or another app, which is extremely useful. But…

A Touch of Caution
------------------

Using the JavaScriptSerializer to pull out a part of your model and convert it into JavaScript is great for showing you how you might go about performing similar actions against a model. Right? Well almost.

The code generated will work nearly all the time, but there are some actions that will not be rendered in exactly the way that you have to write a script updating a model. For example, I have found that the code generated **is not executable against a model** where the script uses the **System** module.

The SDK cannot be used to access the **System** module for reading or writing, which is a complication. There are workarounds that permit you to refer to something in the **System** module, so for example in the domain model of Administration above at the top of the script a domainmodels.Generalization is created which refers to System.User and which is later used when creating the specialization named Account at the bottom of the script. The syntax given in the script is correct but currently will be rejected if you try to run it. You need to replace:

```
generalization1.__generalization.updateWithRawValue("System.User");
```

with:

```
(generalization1 as any)["_generalization"].updateWithRawValue("System.User");
```

There are similar instances with setting Microflow call parameters and referring to attributes in System Entities through specializations. I expect there are other places where this type of issue may come up. These matters are on the backlog for fixing but for the time being you will need to use a workaround, such as this one just above👆.

Summary
-------

I hope you find this blog post and script useful. In my next SDK post, **I will write a script to create a brand-new app**, and **add a module to it** along with **a domain model** and some simple support documents.

The folder and script used to produce this blog post, along with the output from the example commands, are available on [GitHub.](https://github.com/Adrian-Preston/SDKBlog1)

==================================================

# ARTICLE 6: Build widgets in Mendix with React Part 4 – ArcGIS Maps
[Read More](https://www.mendix.com/blog/build-widgets-in-mendix-with-react-part-4-arcgis-maps/)
--------------------------------------------------

#### Mendix is the number one low-code platform, and one of its key strengths is the extensibility it provides. You can use React to incorporate cool third-party libraries and extend your application.

This is blog 4 in a multi-part series, the previous blogs can be found here: [**Build widgets in Mendix with React — Part 1 — Colour Counter**](https://medium.com/mendix/build-widgets-in-mendix-with-react-part-1-colour-counter-f1e400c3cdff "https://medium.com/mendix/build-widgets-in-mendix-with-react-part-1-colour-counter-f1e400c3cdff"), [**Build Widgets in Mendix with React Part 2 — Timer**](https://medium.com/mendix/build-widgets-in-mendix-with-react-part-2-timer-b65c720b34e3 "https://medium.com/mendix/build-widgets-in-mendix-with-react-part-2-timer-b65c720b34e3"), and [**Build Widgets in Mendix with React Part 3 — Kanban**](https://medium.com/mendix/build-widgets-in-mendix-with-react-part-3-kanban-2598aa71444d "https://medium.com/mendix/build-widgets-in-mendix-with-react-part-3-kanban-2598aa71444d").

---

#### 

What are we building
--------------------

Recently, [Ivo Sturm](https://medium.com/u/b43844a7f8d5) wrote a blog about converting an existing ArcGIS widget from Dojo to React.

I thought it would be interesting to **build a simple version of the ArcGIS map widget from scratch**.

![](https://www.mendix.com/wp-content/uploads/1_mNlK3NwAnJIkRtq7JcZbEA.webp)

Get started
-----------

As with all of the pluggable widget blogs up to this point, we begin by **scaffolding our widget** by running `yo @mendix/widget arcGISMap` and [setting up a test Mendix project](https://medium.com/mendix/build-widgets-in-mendix-with-react-part-1-colour-counter-f1e400c3cdff).

Let’s start by **installing the npm package** for the ArcGIS Javascript API

```
npm install @arcgis/core
```

ArcGIS is an online geographic information system that allows you to display maps and add layers to display a whole range of information.

![](https://www.mendix.com/wp-content/uploads/1_nYOeglXLJ6-H30lKfSNiPQ.webp)

In order to access the full service [you need to register and create an access token](https://developers.arcgis.com/documentation/mapping-apis-and-services/get-started/) but we can press on without one for our simple example.

#### Getting started

Reviewing the [documentation](https://developers.arcgis.com/javascript/latest/display-a-map/#create-a-map-view) we can update our code to have two files:

**A parent**

```
import { ReactElement, createElement } from "react";
import { MapComponent } from "./components/Map";
import { ArcGISMapBlogContainerProps } from "../typings/ArcGISMapBlogProps";
import "./ui/ArcGISMapBlog.css";
```

```
export function ArcGISMapBlog(props: ArcGISMapBlogContainerProps): ReactElement {
    return <MapComponent basemap={props.basemap} />;
}
```

**And a child**

```
import { ReactElement, createElement, useEffect, useRef } from "react";
import Map from "@arcgis/core/Map";
import MapView from "@arcgis/core/views/MapView";
import Legend from "@arcgis/core/widgets/Legend";
```

```
export interface MapProps {
    basemap: string;
}
```

```
export function MapComponent({ basemap }: MapProps): ReactElement {
    const mapDiv = useRef(null);
```

```
useEffect(() => {
        if (mapDiv.current) {
            MountMap(basemap);
        }
    }, [basemap]);
```

```
const MountMap = (basemap: string): MapView => {
        const legend = new Legend();
        const map = new Map({ basemap });
        const view = new MapView({
            map,
            center: [0.029, 51.256], // Longitude, latitude
            zoom: 10, // Zoom level
            container: mapDiv.current as unknown as HTMLDivElement 
        });
```

```
        legend.view = view;
        view.ui.add(legend, "bottom-right");
        return view;
    };
```

```
return <div id="viewDiv" ref={mapDiv} style={{height: "500px"}}/>;
}
```

Let’s **also import the stylesheet from ArcGIS** so that we can make our widget look nice, change your UI/{widgetName}.css to:

```
@import "https://js.arcgis.com/4.24/@arcgis/core/assets/esri/themes/dark/main.css";
```

Now we build our widget with `npm run build` and… we get an error:

```
[!] Error: Invalid value for option "output.file" - when building multiple chunks, the "output.dir" option must be used, not "output.file". To inline dynamic imports, set the "inlineDynamicImports" option.
```

So how do we fix this? In order to explain, we need to take a few steps back…

A brief history of Javascript
-----------------------------

This next section is a brief history of Javascript, to give context to the solution, if this is not of interest to you, feel free to skip and continue with the example

In the beginning…

Javascript was invented by Brendan Eich in 1995, and for the first several years of its development, it was used primarily for isolated scripting tasks. As JS started to be used more in applications, it became more difficult to manage the code. JS was used in more complex ways often across multiple scripts, which inevitably led to function and name conflicts.

As such, the module concept was introduced, this meant that code could be written in a closed place for internal use without fear of conflicts elsewhere and also allowed developers to break large codebases down into small separate parts, making it much easier to write and maintain.

The first attempt to fix this was with **Immediately Invoked Function Expressions (IIFE)**, which essentially just wrapped each file in a function, keeping variables and functions within a file, in that scope instead of the global scope.

`(function() {// Your code }) ();`

There are still many problems with this approach, including a lack of dependency resolution and [pollution of the global namespace](https://www.tutorialspoint.com/what-is-global-namespace-pollution-in-javascript#:~:text=Polluting%20Global%20namespace%20causes%20name,be%20using%20several%20javascript%20libraries).

Over time 3 separate (and competing) module specs emerged:

* **CommonJS** — still widely used in Node for server-side JS, and easily recognizable by it’s `require()` and `module.exports` syntax
* **AMD** — Asynchronous Module Definition, split from CommonJS early. The key difference is that AMD allows modules that are not dependent on each other to be loaded async (it’s all in the name!)
* **UMD** — Universal Module Definition, supports both of the other module specs as well as ‘old style’ “global” variable definition

This is all very complicated…so some good news. Since 2015 and the release of ES6, **modules have been supported within the Javascript language**. This gives us the lovely and simple`import` and `export` syntax we have been using in our code.

So why the history lesson? Well, we need to be able to handle all of these module types when we write our code, and that is where bundlers come in.

Bundlers
--------

Bundlers allow you to **compile your code at build time**, **process your dependencies**, and **serve up a compatible concatenated file**. Common solutions for this include **Webpack** (used in Mendix 8 widgets) and **rollup** (used in Mendix 9 widgets)

This lets you write your code modularly using modern ES6 features (and even Typescript if you fancy it) and then produce an optimized file (or set of files) to be served to the browser.

This is great, but some browsers don’t yet support ES6, so they won’t be able to do anything with these nicely compiled files. In order to fix this **we can use a Transpiler** such as **Babel** to serve it to the webpage in a format in which it can be read.

So back to our widgets…

---

The Pluggable Widget framework requires all of the tools you need to develop React components for Mendix apps. This includes:

* **npm** — A package manager to easily install and manage third-party packages
* **rollup** — A bundler, which lets you write your code modularly and then bundle it together in small packages
* **babel** — A transpiler that converts the JS into a format that can be read by older browsers (and Studio Pro)

So what’s our error mean?

```
[!] Error: Invalid value for option "output.file" - when building multiple chunks, the "output.dir" option must be used, not "output.file". To inline dynamic imports, set the "inlineDynamicImports" option.
```

For each widget project, we use the rollup configuration provided by the @mendix/pluggable-widget-tools library.

This can be found in: **node\_modules/@mendix/pluggable-widget-tools/configs.rollup.config.js.**

In this configuration, we are **telling our widget to spit out our compiled JS into a single file**. Meanwhile, the **ArcGIS npm library** we are using provides **dynamic imports in chunks**, which by default **rollup wants to spit out as separate files into a directory**.

To fix this we just need do what it says in the error and **set the inlineDynamicImports option**, which will pull everything into one file. We could change the rollup.config.js file in the Pluggable Widgets library but this is a very bad idea as it is not maintainable, and creates very hard-to-read and debug code. Luckily **Mendix has built-in functionality to set our own rollup config**.

We need to **create a file** called r**ollup.config.js** in the root widget directory. We then add the following JS code to change how our widget is built:

```
export default args => {
    const result = args.configDefaultConfig;
    console.warn ('Custom roll up')
    return result.map((config) => {
                config.output.inlineDynamicImports = true
                console.warn ("Set dynamic imports")
                return config;
    });
};
```

So we run `npm run build` again, and get a new error:

```
FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory
```

Turns out the build process needs more memory. I can update this by running

```
export NODE_OPTIONS=--max_old_space_size=5120
```

If we rebuild then our widget now compiles.

---

Our bundler can help us create single files so that they can be easily read by the browser.

Rollup also does something else very clever, called **Tree Shaking**: this involves building an image of the **dependency tree in your code** and **only including the code that is actually needed**. This is particularly useful when using large libraries, and avoids loading large amounts of unused code into the browser. This tree shaking is one of the key factors Mendix made the switch from webpack to rollup between Mendix 8 and 9.

Bundlers also come with a whole host of other features, in roll-up, these are in the form of plugins. The last thing I want to do in this blog is cover a really common use case for having to modify your rollup config for your widget

Serving up the files your widget needs
--------------------------------------

ArcGIS delivers the files needed to create your map via a **content delivery network (CDN)** . However there may be **instances where you want to keep** **and manage these files within your widget**, perhaps due to do firewall settings within your organization. Fortunately, the ArcGIS Javascript API makes this possible.

The first thing to do is to update our code, to **tell the API** that we will be **managing our assets locally**. To do this we simply update our container component to contain:

```
import esriConfig from "@arcgis/core/config.js";
```

```
export function ArcGISMapBlog(props: ArcGISMapBlogContainerProps): ReactElement {
    esriConfig.assetsPath = "./widgets/mendix/arcgismapblog/assets";
    return <MapComponent basemap={props.basemap} />;
}
```

Next, we need to **update** our **rollup** to **pick up the files we** need from our node modules and **put them in our widget** mpk.

To do this we can **use the rollup copy plugin** (there are plugins for everything), first, we need to install it

```
npm i rollup-plugin-copy —save-dev 
```

We use the `—save-dev` command because it is a dependency only required while developing. Then we update our rollup.config.js to:

```
import copy from "rollup-plugin-copy";
export default args => {
    const result = args.configDefaultConfig;
    console.warn ('Custom roll up')
    return result.map((config) => {
                config.output.inlineDynamicImports = true
                console.warn ("Set dynamic imports")
                const plugins = config.plugins || []
                config.plugins = [
                    ...plugins,
                    copy({
                        targets: { src:"node_modules/@arcgis/core/assets", dest:"dist/tmp/widgets/mendix/arcgismapblog" }]
```

```
}),
                ]  
                return config;
    });
};
```

This **takes the ‘assets’** folder from the ArcGIS npm package and **drops it into our dist/tmp folder** which is what is ultimately zipped to create our mpk. Then when we run our application the contents of the widget mpk are served up to **./widgets/{yourOrganisationName}/{yourWidgetName}**.

To see this in action let’s run the command to build our widget

```
npm run build
```

We can then re-run our app.

![](https://www.mendix.com/wp-content/uploads/1_5YGKygT3y96vxsbg4pW3Ww.webp)

If we open our deployment directory we can see that the widget is serving up the assets folder, and if we check our page sources in our chrome dev tools, we can see that the ArcGIS web assembly file is served up to the browser to ensure our map works

We didn’t update our CSS to use local files. To do this we simply update our file to:

```
@import "../assets/esri/themes/dark/main.css";
```

Simple….kind of….

If you are using the **pluggable widget tools of 9.13.2 or below** and you are using Windows, then your **fonts will not be imported properly**. The following code is required in your rollup.config.js to fix the imports:

```
import postcssUrl from "postcss-url";
```

```
const cssUrlTransform = asset => {
    const outWidgetDirForwardSlash = outWidgetDir.replace(/\\/g, "/")
    return asset.url.startsWith(`${assetsDirName}/`) ? `${outWidgetDirForwardSlash}/${asset.url}` : asset.url;
}
```

```
export default args => {
    const result = args.configDefaultConfig;
    console.warn ('Custom roll up')
    return result.map((config) => {
                config.output.inlineDynamicImports = true
                console.warn ("Set dynamic imports")
                const plugins = config.plugins || []
                config.plugins = [
                    ...plugins,
                    postcssUrl (cssUrlTransform)
```

```
]  
                return config;
    });
};
```

Then run `npm install postcss-url --save-dev` . Your widget will now render with icons.

---

And we are done!

The ArcGIS API is packed full of amazing features, I would encourage you to explore it. To see a great example of what it can do, check out Ivo Sturm’s widget: [**GitHub – ivosturm/ArcGIS-React: A new and improved ArcGIS widget based on React**](https://github.com/ivosturm/ArcGIS-React "https://github.com/ivosturm/ArcGIS-React"). The repo for my ArcGIS widget can be found here: [**GitHub – joe-robertson-mx/arcGISMapBlog**](https://github.com/joe-robertson-mx/arcGISMapBlog "https://github.com/joe-robertson-mx/arcGISMapBlog").

==================================================

