# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 505
- HTTP: 373 alive / 169 gold
- HTTPS: 248 alive / 48 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 212 alive / 145 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19167
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
