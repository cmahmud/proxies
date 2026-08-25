# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 421
- HTTP: 102 alive / 62 gold
- HTTPS: 86 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35763
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
