# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 341
- HTTP: 128 alive / 39 gold
- HTTPS: 108 alive / 8 gold
- SOCKS4: 174 alive / 151 gold
- SOCKS5: 198 alive / 143 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
