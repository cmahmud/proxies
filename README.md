# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 405
- HTTP: 91 alive / 64 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37673
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
