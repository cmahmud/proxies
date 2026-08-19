# SyndProxy private pool

## Current pool

- Alive now: 1217
- Gold now: 412
- HTTP: 403 alive / 82 gold
- HTTPS: 267 alive / 16 gold
- SOCKS4: 274 alive / 150 gold
- SOCKS5: 273 alive / 164 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20633
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
