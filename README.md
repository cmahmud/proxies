# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 409
- HTTP: 103 alive / 69 gold
- HTTPS: 180 alive / 20 gold
- SOCKS4: 179 alive / 156 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40607
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
