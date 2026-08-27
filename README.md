# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 422
- HTTP: 102 alive / 79 gold
- HTTPS: 127 alive / 18 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42143
- Ever gold: 1351

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
