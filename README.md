# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 408
- HTTP: 341 alive / 99 gold
- HTTPS: 226 alive / 21 gold
- SOCKS4: 203 alive / 137 gold
- SOCKS5: 275 alive / 151 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27922
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
