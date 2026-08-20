# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 386
- HTTP: 234 alive / 80 gold
- HTTPS: 160 alive / 22 gold
- SOCKS4: 208 alive / 141 gold
- SOCKS5: 235 alive / 143 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25272
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
