# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 395
- HTTP: 75 alive / 49 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42771
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
