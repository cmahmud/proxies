# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 402
- HTTP: 90 alive / 65 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 174 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37722
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
