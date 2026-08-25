# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 391
- HTTP: 91 alive / 60 gold
- HTTPS: 68 alive / 17 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 168 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37543
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
