# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 376
- HTTP: 100 alive / 66 gold
- HTTPS: 69 alive / 15 gold
- SOCKS4: 152 alive / 143 gold
- SOCKS5: 182 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38805
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
