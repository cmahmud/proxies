# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 405
- HTTP: 128 alive / 71 gold
- HTTPS: 162 alive / 16 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40422
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
