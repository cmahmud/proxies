# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 388
- HTTP: 337 alive / 85 gold
- HTTPS: 180 alive / 15 gold
- SOCKS4: 223 alive / 156 gold
- SOCKS5: 205 alive / 132 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18228
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
