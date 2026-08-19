# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 342
- HTTP: 324 alive / 63 gold
- HTTPS: 205 alive / 12 gold
- SOCKS4: 221 alive / 141 gold
- SOCKS5: 217 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20243
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
