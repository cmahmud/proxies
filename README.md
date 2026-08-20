# SyndProxy private pool

## Current pool

- Alive now: 1571
- Gold now: 647
- HTTP: 608 alive / 242 gold
- HTTPS: 493 alive / 129 gold
- SOCKS4: 208 alive / 133 gold
- SOCKS5: 262 alive / 143 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24571
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
