# SyndProxy private pool

## Current pool

- Alive now: 723
- Gold now: 367
- HTTP: 201 alive / 75 gold
- HTTPS: 117 alive / 19 gold
- SOCKS4: 183 alive / 127 gold
- SOCKS5: 222 alive / 146 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25607
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
