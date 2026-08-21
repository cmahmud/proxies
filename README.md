# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 398
- HTTP: 261 alive / 89 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 234 alive / 152 gold

## Historical pool

- Discovered: 157427
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
