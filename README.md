# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 255
- HTTP: 371 alive / 32 gold
- HTTPS: 153 alive / 4 gold
- SOCKS4: 209 alive / 116 gold
- SOCKS5: 217 alive / 103 gold

## Historical pool

- Discovered: 95404
- Ever alive: 10934
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
