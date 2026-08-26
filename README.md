# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 386
- HTTP: 118 alive / 64 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 181 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39330
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
