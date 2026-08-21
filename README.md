# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 453
- HTTP: 333 alive / 108 gold
- HTTPS: 193 alive / 30 gold
- SOCKS4: 208 alive / 154 gold
- SOCKS5: 251 alive / 161 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28587
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
