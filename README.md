# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 392
- HTTP: 364 alive / 84 gold
- HTTPS: 247 alive / 21 gold
- SOCKS4: 200 alive / 133 gold
- SOCKS5: 241 alive / 154 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24977
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
