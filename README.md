# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 359
- HTTP: 66 alive / 48 gold
- HTTPS: 50 alive / 10 gold
- SOCKS4: 164 alive / 148 gold
- SOCKS5: 167 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43515
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
