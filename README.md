# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 477
- HTTP: 321 alive / 124 gold
- HTTPS: 240 alive / 70 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 240 alive / 142 gold

## Historical pool

- Discovered: 113910
- Ever alive: 16905
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
