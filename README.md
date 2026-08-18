# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 255
- HTTP: 367 alive / 32 gold
- HTTPS: 99 alive / 4 gold
- SOCKS4: 206 alive / 116 gold
- SOCKS5: 210 alive / 103 gold

## Historical pool

- Discovered: 95404
- Ever alive: 10863
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
