# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 421
- HTTP: 327 alive / 90 gold
- HTTPS: 201 alive / 28 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 250 alive / 158 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31555
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
