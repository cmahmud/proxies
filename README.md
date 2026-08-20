# SyndProxy private pool

## Current pool

- Alive now: 1426
- Gold now: 561
- HTTP: 568 alive / 174 gold
- HTTPS: 389 alive / 90 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 247 alive / 163 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23056
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
