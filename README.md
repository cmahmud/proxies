# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 399
- HTTP: 77 alive / 53 gold
- HTTPS: 46 alive / 19 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41681
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
