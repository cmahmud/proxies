# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 396
- HTTP: 183 alive / 73 gold
- HTTPS: 142 alive / 19 gold
- SOCKS4: 214 alive / 156 gold
- SOCKS5: 209 alive / 148 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26742
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
