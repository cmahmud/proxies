# SyndProxy private pool

## Current pool

- Alive now: 1289
- Gold now: 416
- HTTP: 459 alive / 83 gold
- HTTPS: 294 alive / 17 gold
- SOCKS4: 236 alive / 158 gold
- SOCKS5: 300 alive / 158 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21892
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
