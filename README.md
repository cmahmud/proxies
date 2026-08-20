# SyndProxy private pool

## Current pool

- Alive now: 1412
- Gold now: 601
- HTTP: 569 alive / 197 gold
- HTTPS: 380 alive / 98 gold
- SOCKS4: 210 alive / 140 gold
- SOCKS5: 253 alive / 166 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23110
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
