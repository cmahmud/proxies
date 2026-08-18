# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 289
- HTTP: 242 alive / 27 gold
- HTTPS: 132 alive / 6 gold
- SOCKS4: 246 alive / 146 gold
- SOCKS5: 222 alive / 110 gold

## Historical pool

- Discovered: 99931
- Ever alive: 12363
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
