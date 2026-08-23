# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 343
- HTTP: 96 alive / 38 gold
- HTTPS: 61 alive / 10 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 170 alive / 143 gold

## Historical pool

- Discovered: 171059
- Ever alive: 32857
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
