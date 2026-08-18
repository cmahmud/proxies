# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 209
- HTTP: 443 alive / 25 gold
- HTTPS: 156 alive / 9 gold
- SOCKS4: 217 alive / 95 gold
- SOCKS5: 228 alive / 80 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7957
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
