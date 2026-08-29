# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 359
- HTTP: 53 alive / 34 gold
- HTTPS: 28 alive / 6 gold
- SOCKS4: 161 alive / 157 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43575
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
