# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 446
- HTTP: 324 alive / 97 gold
- HTTPS: 212 alive / 33 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 271 alive / 166 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31270
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
