# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 405
- HTTP: 368 alive / 94 gold
- HTTPS: 252 alive / 17 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 332 alive / 147 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21201
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
