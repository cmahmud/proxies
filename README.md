# SyndProxy private pool

## Current pool

- Alive now: 649
- Gold now: 240
- HTTP: 174 alive / 38 gold
- HTTPS: 87 alive / 7 gold
- SOCKS4: 202 alive / 124 gold
- SOCKS5: 186 alive / 71 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9365
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
