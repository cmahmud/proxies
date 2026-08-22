# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 401
- HTTP: 219 alive / 86 gold
- HTTPS: 141 alive / 27 gold
- SOCKS4: 223 alive / 132 gold
- SOCKS5: 250 alive / 156 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31645
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
