# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 201
- HTTP: 148 alive / 23 gold
- HTTPS: 123 alive / 9 gold
- SOCKS4: 205 alive / 89 gold
- SOCKS5: 208 alive / 80 gold

## Historical pool

- Discovered: 89658
- Ever alive: 7999
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
