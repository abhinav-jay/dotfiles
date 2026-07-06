#!/usr/bin/env node

const { execSync } = require("child_process");

function getWorkspaces() {
    const data = JSON.parse(execSync("hyprctl workspaces -j").toString());
    return data.map(ws => ws.id).sort((a, b) => a - b);
}

function getActive() {
    const data = JSON.parse(execSync("hyprctl activeworkspace -j").toString());
    return data.id;
}

function render() {
    const workspaces = getWorkspaces();
    const active = getActive();

    const buttons = workspaces.map(id => {
        return `<span class="ws">${id}</span>`;
    }).join("");

    const index = workspaces.indexOf(active);
    const offset = index * 36; // tweak if spacing changes

    return JSON.stringify({
        text: `
            <div id="ws-container">
                <div id="ws-highlight" style="transform: translateX(${offset}px)"></div>
                ${buttons}
            </div>
        `
    });
}

console.log(render());
