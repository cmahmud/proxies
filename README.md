# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 383
- HTTP: 175 alive / 69 gold
- HTTPS: 88 alive / 15 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 218 alive / 158 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
