# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 471
- HTTP: 130 alive / 94 gold
- HTTPS: 118 alive / 39 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46361
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
