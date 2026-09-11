# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 352
- HTTP: 106 alive / 78 gold
- HTTPS: 51 alive / 26 gold
- SOCKS4: 80 alive / 76 gold
- SOCKS5: 178 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48677
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
