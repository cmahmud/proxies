# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 333
- HTTP: 103 alive / 40 gold
- HTTPS: 81 alive / 6 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 185 alive / 137 gold

## Historical pool

- Discovered: 171578
- Ever alive: 32895
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
