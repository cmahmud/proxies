# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 257
- HTTP: 216 alive / 31 gold
- HTTPS: 89 alive / 7 gold
- SOCKS4: 194 alive / 130 gold
- SOCKS5: 189 alive / 89 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9161
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
