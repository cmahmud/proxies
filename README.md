# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 420
- HTTP: 95 alive / 70 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 217 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37125
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
