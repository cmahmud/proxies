# SyndProxy private pool

## Current pool

- Alive now: 1891
- Gold now: 620
- HTTP: 825 alive / 239 gold
- HTTPS: 617 alive / 116 gold
- SOCKS4: 190 alive / 103 gold
- SOCKS5: 259 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24775
- Ever gold: 1038

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
