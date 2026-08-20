# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 367
- HTTP: 195 alive / 75 gold
- HTTPS: 111 alive / 20 gold
- SOCKS4: 178 alive / 127 gold
- SOCKS5: 218 alive / 145 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1068

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
