# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 393
- HTTP: 80 alive / 51 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41624
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
