# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 375
- HTTP: 285 alive / 83 gold
- HTTPS: 227 alive / 26 gold
- SOCKS4: 230 alive / 125 gold
- SOCKS5: 230 alive / 141 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32119
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
