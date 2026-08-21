# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 402
- HTTP: 324 alive / 95 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 263 alive / 150 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27908
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
