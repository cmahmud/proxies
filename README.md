# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 416
- HTTP: 91 alive / 69 gold
- HTTPS: 107 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42532
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
