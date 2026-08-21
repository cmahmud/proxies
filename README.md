# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 402
- HTTP: 234 alive / 91 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 211 alive / 140 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27766
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
