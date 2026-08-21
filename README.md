# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 369
- HTTP: 303 alive / 93 gold
- HTTPS: 210 alive / 23 gold
- SOCKS4: 212 alive / 140 gold
- SOCKS5: 211 alive / 113 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28990
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
