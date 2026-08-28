# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 393
- HTTP: 102 alive / 70 gold
- HTTPS: 82 alive / 11 gold
- SOCKS4: 162 alive / 157 gold
- SOCKS5: 171 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43106
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
