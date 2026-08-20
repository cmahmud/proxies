# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 392
- HTTP: 360 alive / 84 gold
- HTTPS: 243 alive / 21 gold
- SOCKS4: 198 alive / 133 gold
- SOCKS5: 242 alive / 154 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24977
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
