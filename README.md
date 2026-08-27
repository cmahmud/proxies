# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 400
- HTTP: 98 alive / 57 gold
- HTTPS: 104 alive / 17 gold
- SOCKS4: 182 alive / 167 gold
- SOCKS5: 193 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41520
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
