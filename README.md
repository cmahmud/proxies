# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 376
- HTTP: 102 alive / 66 gold
- HTTPS: 70 alive / 15 gold
- SOCKS4: 150 alive / 143 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38805
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
