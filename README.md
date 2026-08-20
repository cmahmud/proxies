# SyndProxy private pool

## Current pool

- Alive now: 670
- Gold now: 355
- HTTP: 166 alive / 63 gold
- HTTPS: 134 alive / 16 gold
- SOCKS4: 184 alive / 134 gold
- SOCKS5: 186 alive / 142 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26673
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
