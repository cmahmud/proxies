# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 373
- HTTP: 78 alive / 47 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 173062
- Ever alive: 33007
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
