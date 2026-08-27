# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 417
- HTTP: 99 alive / 67 gold
- HTTPS: 143 alive / 19 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41231
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
