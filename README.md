# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 415
- HTTP: 213 alive / 85 gold
- HTTPS: 180 alive / 21 gold
- SOCKS4: 232 alive / 155 gold
- SOCKS5: 243 alive / 154 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27577
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
