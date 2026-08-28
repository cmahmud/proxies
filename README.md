# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 403
- HTTP: 75 alive / 55 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42780
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
