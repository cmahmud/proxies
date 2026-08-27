# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 417
- HTTP: 113 alive / 70 gold
- HTTPS: 151 alive / 18 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41222
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
