# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 236
- HTTP: 217 alive / 37 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 204 alive / 124 gold
- SOCKS5: 197 alive / 68 gold

## Historical pool

- Discovered: 94340
- Ever alive: 9418
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
