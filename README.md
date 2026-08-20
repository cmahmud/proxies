# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 367
- HTTP: 177 alive / 69 gold
- HTTPS: 143 alive / 19 gold
- SOCKS4: 183 alive / 120 gold
- SOCKS5: 229 alive / 159 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26045
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
