# SyndProxy private pool

## Current pool

- Alive now: 671
- Gold now: 365
- HTTP: 160 alive / 66 gold
- HTTPS: 119 alive / 17 gold
- SOCKS4: 183 alive / 141 gold
- SOCKS5: 209 alive / 141 gold

## Historical pool

- Discovered: 147648
- Ever alive: 25872
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
