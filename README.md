# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 394
- HTTP: 93 alive / 62 gold
- HTTPS: 79 alive / 17 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37546
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
