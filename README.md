# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 238
- HTTP: 348 alive / 30 gold
- HTTPS: 67 alive / 7 gold
- SOCKS4: 180 alive / 110 gold
- SOCKS5: 188 alive / 91 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8882
- Ever gold: 359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
