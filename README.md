# SyndProxy private pool

## Current pool

- Alive now: 1277
- Gold now: 417
- HTTP: 476 alive / 103 gold
- HTTPS: 323 alive / 30 gold
- SOCKS4: 231 alive / 152 gold
- SOCKS5: 247 alive / 132 gold

## Historical pool

- Discovered: 159263
- Ever alive: 30344
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
