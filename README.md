# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 393
- HTTP: 99 alive / 62 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37418
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
