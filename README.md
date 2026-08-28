# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 430
- HTTP: 119 alive / 82 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42257
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
