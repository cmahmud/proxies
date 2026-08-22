# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 408
- HTTP: 232 alive / 93 gold
- HTTPS: 172 alive / 30 gold
- SOCKS4: 210 alive / 131 gold
- SOCKS5: 234 alive / 154 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31937
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
