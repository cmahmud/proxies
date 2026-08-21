# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 348
- HTTP: 252 alive / 76 gold
- HTTPS: 168 alive / 21 gold
- SOCKS4: 199 alive / 119 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 157604
- Ever alive: 29778
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
