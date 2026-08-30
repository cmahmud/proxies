# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 431
- HTTP: 101 alive / 81 gold
- HTTPS: 66 alive / 24 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44527
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
