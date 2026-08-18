# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 284
- HTTP: 364 alive / 28 gold
- HTTPS: 210 alive / 4 gold
- SOCKS4: 229 alive / 134 gold
- SOCKS5: 246 alive / 118 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12710
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
