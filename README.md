# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 503
- HTTP: 322 alive / 147 gold
- HTTPS: 261 alive / 87 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 208 alive / 130 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17611
- Ever gold: 691

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
