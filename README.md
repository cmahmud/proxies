# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 395
- HTTP: 351 alive / 96 gold
- HTTPS: 296 alive / 31 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 226 alive / 118 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30283
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
