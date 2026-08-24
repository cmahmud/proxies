# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 415
- HTTP: 110 alive / 75 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33721
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
