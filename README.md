# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 438
- HTTP: 151 alive / 77 gold
- HTTPS: 102 alive / 28 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 217 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45411
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
