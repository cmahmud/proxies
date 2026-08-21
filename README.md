# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 415
- HTTP: 276 alive / 83 gold
- HTTPS: 188 alive / 23 gold
- SOCKS4: 208 alive / 151 gold
- SOCKS5: 244 alive / 158 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28909
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
