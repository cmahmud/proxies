# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 278
- HTTP: 302 alive / 63 gold
- HTTPS: 233 alive / 18 gold
- SOCKS4: 190 alive / 99 gold
- SOCKS5: 191 alive / 98 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15415
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
