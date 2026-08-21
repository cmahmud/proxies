# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 408
- HTTP: 281 alive / 83 gold
- HTTPS: 214 alive / 18 gold
- SOCKS4: 232 alive / 161 gold
- SOCKS5: 227 alive / 146 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30026
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
