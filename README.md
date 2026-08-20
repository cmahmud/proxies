# SyndProxy private pool

## Current pool

- Alive now: 1628
- Gold now: 608
- HTTP: 584 alive / 217 gold
- HTTPS: 468 alive / 112 gold
- SOCKS4: 210 alive / 135 gold
- SOCKS5: 366 alive / 144 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23905
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
