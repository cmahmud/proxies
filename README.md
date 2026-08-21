# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 418
- HTTP: 313 alive / 86 gold
- HTTPS: 226 alive / 28 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 244 alive / 161 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29430
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
