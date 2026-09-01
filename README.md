# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 471
- HTTP: 139 alive / 95 gold
- HTTPS: 115 alive / 37 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46886
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
