# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 428
- HTTP: 336 alive / 107 gold
- HTTPS: 197 alive / 28 gold
- SOCKS4: 250 alive / 149 gold
- SOCKS5: 262 alive / 144 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30796
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
