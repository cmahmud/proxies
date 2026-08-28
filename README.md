# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 403
- HTTP: 75 alive / 55 gold
- HTTPS: 62 alive / 23 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42776
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
