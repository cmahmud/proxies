# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 341
- HTTP: 96 alive / 38 gold
- HTTPS: 63 alive / 10 gold
- SOCKS4: 168 alive / 150 gold
- SOCKS5: 169 alive / 143 gold

## Historical pool

- Discovered: 171059
- Ever alive: 32857
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
