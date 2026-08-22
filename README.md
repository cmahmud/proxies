# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 388
- HTTP: 216 alive / 90 gold
- HTTPS: 142 alive / 27 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 213 alive / 131 gold

## Historical pool

- Discovered: 163259
- Ever alive: 31778
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
