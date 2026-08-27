# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 411
- HTTP: 115 alive / 67 gold
- HTTPS: 166 alive / 15 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41151
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
