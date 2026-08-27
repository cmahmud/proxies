# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 418
- HTTP: 113 alive / 70 gold
- HTTPS: 152 alive / 19 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41223
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
