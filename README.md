# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 506
- HTTP: 361 alive / 157 gold
- HTTPS: 260 alive / 90 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 211 alive / 118 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18372
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
