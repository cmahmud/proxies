# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 367
- HTTP: 187 alive / 66 gold
- HTTPS: 137 alive / 17 gold
- SOCKS4: 200 alive / 134 gold
- SOCKS5: 205 alive / 150 gold

## Historical pool

- Discovered: 145550
- Ever alive: 25408
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
