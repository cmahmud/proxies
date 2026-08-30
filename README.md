# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 428
- HTTP: 100 alive / 79 gold
- HTTPS: 63 alive / 24 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44527
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
