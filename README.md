# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 454
- HTTP: 127 alive / 86 gold
- HTTPS: 118 alive / 30 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46716
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
