# SyndProxy private pool

## Current pool

- Alive now: 1200
- Gold now: 407
- HTTP: 434 alive / 90 gold
- HTTPS: 257 alive / 17 gold
- SOCKS4: 229 alive / 143 gold
- SOCKS5: 280 alive / 157 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20868
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
