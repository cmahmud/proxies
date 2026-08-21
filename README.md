# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 413
- HTTP: 394 alive / 107 gold
- HTTPS: 288 alive / 31 gold
- SOCKS4: 195 alive / 124 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28364
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
