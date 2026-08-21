# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 427
- HTTP: 376 alive / 92 gold
- HTTPS: 212 alive / 26 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 233 alive / 159 gold

## Historical pool

- Discovered: 156425
- Ever alive: 29498
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
