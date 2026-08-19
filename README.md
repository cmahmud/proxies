# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 418
- HTTP: 342 alive / 88 gold
- HTTPS: 284 alive / 16 gold
- SOCKS4: 217 alive / 158 gold
- SOCKS5: 301 alive / 156 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21833
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
