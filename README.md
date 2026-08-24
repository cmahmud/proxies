# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 391
- HTTP: 149 alive / 56 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 180 alive / 155 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33640
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
