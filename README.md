# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 416
- HTTP: 103 alive / 73 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41971
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
