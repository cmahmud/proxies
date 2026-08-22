# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 408
- HTTP: 222 alive / 94 gold
- HTTPS: 161 alive / 30 gold
- SOCKS4: 208 alive / 131 gold
- SOCKS5: 232 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31935
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
