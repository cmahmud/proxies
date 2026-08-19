# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 544
- HTTP: 464 alive / 187 gold
- HTTPS: 300 alive / 112 gold
- SOCKS4: 210 alive / 114 gold
- SOCKS5: 197 alive / 131 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19403
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
