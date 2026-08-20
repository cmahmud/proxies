# SyndProxy private pool

## Current pool

- Alive now: 1688
- Gold now: 648
- HTTP: 634 alive / 210 gold
- HTTPS: 482 alive / 122 gold
- SOCKS4: 235 alive / 154 gold
- SOCKS5: 337 alive / 162 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24191
- Ever gold: 970

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
