# SyndProxy private pool

## Current pool

- Alive now: 1561
- Gold now: 610
- HTTP: 567 alive / 208 gold
- HTTPS: 428 alive / 116 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 343 alive / 137 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23665
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
