# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 406
- HTTP: 102 alive / 62 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39114
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
