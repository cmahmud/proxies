# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 416
- HTTP: 111 alive / 71 gold
- HTTPS: 112 alive / 15 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42572
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
