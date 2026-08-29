# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 406
- HTTP: 106 alive / 71 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43653
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
