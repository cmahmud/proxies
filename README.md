# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 414
- HTTP: 265 alive / 85 gold
- HTTPS: 174 alive / 27 gold
- SOCKS4: 185 alive / 132 gold
- SOCKS5: 257 alive / 170 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31488
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
