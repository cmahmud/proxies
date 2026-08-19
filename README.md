# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 531
- HTTP: 397 alive / 158 gold
- HTTPS: 246 alive / 84 gold
- SOCKS4: 230 alive / 151 gold
- SOCKS5: 203 alive / 138 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18042
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
