# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 392
- HTTP: 310 alive / 89 gold
- HTTPS: 179 alive / 30 gold
- SOCKS4: 227 alive / 150 gold
- SOCKS5: 226 alive / 123 gold

## Historical pool

- Discovered: 160987
- Ever alive: 30873
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
