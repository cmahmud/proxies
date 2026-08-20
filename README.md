# SyndProxy private pool

## Current pool

- Alive now: 1590
- Gold now: 642
- HTTP: 606 alive / 216 gold
- HTTPS: 503 alive / 120 gold
- SOCKS4: 242 alive / 156 gold
- SOCKS5: 239 alive / 150 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23762
- Ever gold: 957

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
