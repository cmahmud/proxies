# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 374
- HTTP: 198 alive / 76 gold
- HTTPS: 108 alive / 19 gold
- SOCKS4: 189 alive / 133 gold
- SOCKS5: 233 alive / 146 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1068

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
