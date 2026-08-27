# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 408
- HTTP: 88 alive / 63 gold
- HTTPS: 62 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41727
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
