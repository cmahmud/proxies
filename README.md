# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 411
- HTTP: 82 alive / 63 gold
- HTTPS: 95 alive / 24 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47227
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
