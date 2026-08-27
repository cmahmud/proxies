# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 407
- HTTP: 137 alive / 70 gold
- HTTPS: 167 alive / 14 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40534
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
