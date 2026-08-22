# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 453
- HTTP: 281 alive / 100 gold
- HTTPS: 159 alive / 28 gold
- SOCKS4: 234 alive / 159 gold
- SOCKS5: 240 alive / 166 gold

## Historical pool

- Discovered: 167121
- Ever alive: 32535
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
