# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 392
- HTTP: 88 alive / 61 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41740
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
