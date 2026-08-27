# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 398
- HTTP: 87 alive / 53 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41640
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
