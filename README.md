# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 532
- HTTP: 401 alive / 160 gold
- HTTPS: 266 alive / 89 gold
- SOCKS4: 227 alive / 154 gold
- SOCKS5: 208 alive / 129 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18210
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
