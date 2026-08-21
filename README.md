# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 395
- HTTP: 320 alive / 94 gold
- HTTPS: 271 alive / 33 gold
- SOCKS4: 222 alive / 150 gold
- SOCKS5: 227 alive / 118 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30289
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
