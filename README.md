# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 421
- HTTP: 105 alive / 64 gold
- HTTPS: 85 alive / 23 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35752
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
