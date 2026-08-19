# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 529
- HTTP: 450 alive / 156 gold
- HTTPS: 263 alive / 87 gold
- SOCKS4: 245 alive / 151 gold
- SOCKS5: 210 alive / 135 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18007
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
