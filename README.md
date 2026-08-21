# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 404
- HTTP: 325 alive / 96 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 263 alive / 151 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27908
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
