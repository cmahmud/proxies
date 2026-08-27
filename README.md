# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 395
- HTTP: 80 alive / 53 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41582
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
