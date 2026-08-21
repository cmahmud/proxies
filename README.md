# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 401
- HTTP: 217 alive / 90 gold
- HTTPS: 160 alive / 25 gold
- SOCKS4: 196 alive / 127 gold
- SOCKS5: 219 alive / 159 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27705
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
