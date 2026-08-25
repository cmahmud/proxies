# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 421
- HTTP: 103 alive / 62 gold
- HTTPS: 82 alive / 24 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35764
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
