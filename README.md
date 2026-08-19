# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 514
- HTTP: 364 alive / 151 gold
- HTTPS: 257 alive / 85 gold
- SOCKS4: 196 alive / 135 gold
- SOCKS5: 208 alive / 143 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
