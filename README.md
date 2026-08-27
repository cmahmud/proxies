# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 406
- HTTP: 100 alive / 59 gold
- HTTPS: 111 alive / 19 gold
- SOCKS4: 182 alive / 167 gold
- SOCKS5: 194 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41520
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
