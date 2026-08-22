# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 388
- HTTP: 315 alive / 91 gold
- HTTPS: 238 alive / 34 gold
- SOCKS4: 201 alive / 135 gold
- SOCKS5: 231 alive / 128 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31282
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
