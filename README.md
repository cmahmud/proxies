# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 391
- HTTP: 94 alive / 58 gold
- HTTPS: 64 alive / 15 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33502
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
