# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 394
- HTTP: 75 alive / 48 gold
- HTTPS: 64 alive / 20 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42771
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
