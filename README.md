# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 280
- HTTP: 407 alive / 28 gold
- HTTPS: 146 alive / 5 gold
- SOCKS4: 243 alive / 134 gold
- SOCKS5: 218 alive / 113 gold

## Historical pool

- Discovered: 100094
- Ever alive: 12610
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
