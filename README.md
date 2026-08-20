# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 367
- HTTP: 200 alive / 74 gold
- HTTPS: 110 alive / 20 gold
- SOCKS4: 179 alive / 127 gold
- SOCKS5: 231 alive / 146 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1068

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
