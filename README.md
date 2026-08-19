# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 420
- HTTP: 394 alive / 87 gold
- HTTPS: 293 alive / 16 gold
- SOCKS4: 227 alive / 158 gold
- SOCKS5: 304 alive / 159 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21833
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
