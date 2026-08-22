# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 406
- HTTP: 324 alive / 77 gold
- HTTPS: 250 alive / 22 gold
- SOCKS4: 226 alive / 151 gold
- SOCKS5: 264 alive / 156 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32293
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
