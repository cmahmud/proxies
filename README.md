# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 415
- HTTP: 226 alive / 89 gold
- HTTPS: 178 alive / 25 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 219 alive / 161 gold

## Historical pool

- Discovered: 151686
- Ever alive: 27716
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
