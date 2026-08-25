# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 393
- HTTP: 96 alive / 61 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 171 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37246
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
