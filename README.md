# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 525
- HTTP: 396 alive / 148 gold
- HTTPS: 299 alive / 108 gold
- SOCKS4: 212 alive / 144 gold
- SOCKS5: 197 alive / 125 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 806

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
