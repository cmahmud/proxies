# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 383
- HTTP: 101 alive / 66 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48176
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
