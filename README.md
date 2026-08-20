# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 390
- HTTP: 246 alive / 79 gold
- HTTPS: 206 alive / 27 gold
- SOCKS4: 191 alive / 131 gold
- SOCKS5: 243 alive / 153 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24955
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
