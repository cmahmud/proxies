# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 196
- HTTP: 335 alive / 22 gold
- HTTPS: 100 alive / 7 gold
- SOCKS4: 160 alive / 97 gold
- SOCKS5: 186 alive / 70 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8199
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
