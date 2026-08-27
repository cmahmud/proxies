# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 407
- HTTP: 93 alive / 66 gold
- HTTPS: 79 alive / 17 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41749
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
