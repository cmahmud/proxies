# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 365
- HTTP: 75 alive / 40 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 176 alive / 154 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32984
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
