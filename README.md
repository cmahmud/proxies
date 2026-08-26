# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 377
- HTTP: 121 alive / 67 gold
- HTTPS: 167 alive / 15 gold
- SOCKS4: 158 alive / 146 gold
- SOCKS5: 170 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39788
- Ever gold: 1303

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
