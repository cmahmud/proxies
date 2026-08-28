# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 416
- HTTP: 96 alive / 69 gold
- HTTPS: 102 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42540
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
