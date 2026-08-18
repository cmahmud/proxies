# SyndProxy private pool

## Current pool

- Alive now: 621
- Gold now: 223
- HTTP: 195 alive / 33 gold
- HTTPS: 103 alive / 10 gold
- SOCKS4: 163 alive / 105 gold
- SOCKS5: 160 alive / 75 gold

## Historical pool

- Discovered: 86653
- Ever alive: 5728
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
