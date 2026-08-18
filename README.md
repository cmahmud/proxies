# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 265
- HTTP: 215 alive / 31 gold
- HTTPS: 175 alive / 3 gold
- SOCKS4: 227 alive / 120 gold
- SOCKS5: 239 alive / 111 gold

## Historical pool

- Discovered: 99162
- Ever alive: 12118
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
