const mustache = require('mustache')
const { getImage } = require('random-reddit')
const fs = require('fs')

const generateReadme = async () => {
	const image = await getImage('ProgrammerHumor')
	const template = fs.readFileSync('./main.mustache', 'utf8')
	const readme = mustache.render(template, { image })
	fs.writeFileSync('./README.md', readme)
}

generateReadme()
