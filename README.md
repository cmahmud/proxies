# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 405
- HTTP: 297 alive / 88 gold
- HTTPS: 223 alive / 24 gold
- SOCKS4: 221 alive / 134 gold
- SOCKS5: 265 alive / 159 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31332
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
