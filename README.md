# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 378
- HTTP: 261 alive / 77 gold
- HTTPS: 197 alive / 26 gold
- SOCKS4: 191 alive / 129 gold
- SOCKS5: 201 alive / 146 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31349
- Ever gold: 1158

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
