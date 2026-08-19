# SyndProxy private pool

## Current pool

- Alive now: 1265
- Gold now: 527
- HTTP: 464 alive / 183 gold
- HTTPS: 355 alive / 63 gold
- SOCKS4: 206 alive / 122 gold
- SOCKS5: 240 alive / 159 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19603
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
