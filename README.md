# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 427
- HTTP: 298 alive / 105 gold
- HTTPS: 173 alive / 31 gold
- SOCKS4: 227 alive / 150 gold
- SOCKS5: 244 alive / 141 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30755
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
