# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 407
- HTTP: 110 alive / 62 gold
- HTTPS: 141 alive / 16 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41243
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
