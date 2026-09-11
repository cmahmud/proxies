# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 349
- HTTP: 106 alive / 70 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 92 alive / 89 gold
- SOCKS5: 174 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48691
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
