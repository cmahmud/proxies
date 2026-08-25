# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 396
- HTTP: 102 alive / 65 gold
- HTTPS: 85 alive / 17 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 170 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37342
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
