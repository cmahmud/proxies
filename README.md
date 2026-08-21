# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 368
- HTTP: 322 alive / 82 gold
- HTTPS: 191 alive / 20 gold
- SOCKS4: 207 alive / 126 gold
- SOCKS5: 219 alive / 140 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29815
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
