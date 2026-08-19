# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 339
- HTTP: 315 alive / 57 gold
- HTTPS: 197 alive / 14 gold
- SOCKS4: 214 alive / 134 gold
- SOCKS5: 199 alive / 134 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20037
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
