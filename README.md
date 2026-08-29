# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 398
- HTTP: 89 alive / 68 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 172 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43313
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
