# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 410
- HTTP: 102 alive / 71 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 167 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37189
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
