# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 401
- HTTP: 169 alive / 76 gold
- HTTPS: 137 alive / 19 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 222 alive / 159 gold

## Historical pool

- Discovered: 148155
- Ever alive: 25998
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
