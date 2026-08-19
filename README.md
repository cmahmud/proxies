# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 479
- HTTP: 340 alive / 123 gold
- HTTPS: 227 alive / 70 gold
- SOCKS4: 223 alive / 138 gold
- SOCKS5: 260 alive / 148 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16872
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
