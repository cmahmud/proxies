# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 264
- HTTP: 223 alive / 31 gold
- HTTPS: 123 alive / 5 gold
- SOCKS4: 204 alive / 123 gold
- SOCKS5: 227 alive / 105 gold

## Historical pool

- Discovered: 99053
- Ever alive: 11098
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
