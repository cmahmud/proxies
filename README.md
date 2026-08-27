# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 394
- HTTP: 81 alive / 53 gold
- HTTPS: 56 alive / 18 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41581
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
