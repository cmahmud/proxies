# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 403
- HTTP: 88 alive / 69 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 165 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37193
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
