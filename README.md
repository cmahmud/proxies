# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 267
- HTTP: 198 alive / 32 gold
- HTTPS: 109 alive / 4 gold
- SOCKS4: 206 alive / 133 gold
- SOCKS5: 184 alive / 98 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10667
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
