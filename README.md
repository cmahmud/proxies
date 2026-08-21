# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 393
- HTTP: 215 alive / 91 gold
- HTTPS: 151 alive / 19 gold
- SOCKS4: 216 alive / 129 gold
- SOCKS5: 218 alive / 154 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27767
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
