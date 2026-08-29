# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 360
- HTTP: 89 alive / 51 gold
- HTTPS: 52 alive / 16 gold
- SOCKS4: 152 alive / 148 gold
- SOCKS5: 160 alive / 145 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
