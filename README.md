# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 407
- HTTP: 113 alive / 63 gold
- HTTPS: 150 alive / 17 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41253
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
