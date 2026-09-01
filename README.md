# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 454
- HTTP: 120 alive / 87 gold
- HTTPS: 120 alive / 29 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46716
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
