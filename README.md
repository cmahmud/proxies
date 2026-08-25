# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 415
- HTTP: 105 alive / 61 gold
- HTTPS: 86 alive / 24 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35791
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
