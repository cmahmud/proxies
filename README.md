# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 394
- HTTP: 75 alive / 54 gold
- HTTPS: 57 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42796
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
