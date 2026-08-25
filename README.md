# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 420
- HTTP: 101 alive / 62 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35757
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
