# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 402
- HTTP: 74 alive / 54 gold
- HTTPS: 61 alive / 22 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42776
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
