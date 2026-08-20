# SyndProxy private pool

## Current pool

- Alive now: 1643
- Gold now: 625
- HTTP: 617 alive / 234 gold
- HTTPS: 520 alive / 129 gold
- SOCKS4: 197 alive / 99 gold
- SOCKS5: 309 alive / 163 gold

## Historical pool

- Discovered: 142748
- Ever alive: 24666
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
