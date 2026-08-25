# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 415
- HTTP: 84 alive / 61 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36194
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
