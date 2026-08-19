# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 529
- HTTP: 341 alive / 156 gold
- HTTPS: 252 alive / 92 gold
- SOCKS4: 208 alive / 147 gold
- SOCKS5: 210 alive / 134 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19897
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
