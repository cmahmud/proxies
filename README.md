# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 398
- HTTP: 73 alive / 53 gold
- HTTPS: 49 alive / 19 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41681
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
