# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 420
- HTTP: 93 alive / 71 gold
- HTTPS: 104 alive / 20 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42554
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
