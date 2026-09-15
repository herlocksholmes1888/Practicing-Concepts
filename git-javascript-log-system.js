/*
This was my solution. I couldn't grasp why it wasn't working, since most of the concepts were pretty straightforward from the challenge description

function solution(logs) {
    let counter = 0;
    let files = [];
    let pushPerBranch = [];
       
    for (let i = 0; i < logs.length; i++) {
        if (logs[i].startsWith('push')) {
            const fileName = logs[i].split(' ')[1];
            
            const doesFileExist = files.includes(fileName);
            
            if (doesFileExist !== undefined) {
                files.push(fileName);
                counter = counter + 1;
            } 
        }
        
        if (logs[i].startsWith('switch')) {
            pushPerBranch.push(counter);
            counter = 0;
        }
    }
    
    
    return pushPerBranch
}
*/ 

// This was the solution I've asked ChatGPT. I was obsessed with knowing what exactly I've gotten wrong, since it was an easy challenge and I couldn't understand where I had gotten things wrong.
// Turns out my gut feeling was right: I had made a mistake when verifying if it was a new branch. I wasn't counting the pushes with unique files properly. 

function solution(logs) {
    let currentBranch = "";
    let files = [];
    let maxBranch = "";
    let maxFiles = 0;

    for (const log of logs) {
        if (log.startsWith("switch")) {
            if (files.length > maxFiles) {
                maxFiles = files.length;
                maxBranch = currentBranch;
            }

            currentBranch = log.split(" ")[1];
            files = [];
        } else if (log.startsWith("push")) {
            const fileName = log.split(" ")[1];

            if (!files.includes(fileName)) {
                files.push(fileName);
            }
        }
    }

    // Check the last branch
    if (files.length > maxFiles) {
        maxBranch = currentBranch;
    }

    return maxBranch;
}
