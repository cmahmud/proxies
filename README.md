# SyndProxy private pool

## Current pool

- Alive now: 1204
- Gold now: 422
- HTTP: 426 alive / 121 gold
- HTTPS: 302 alive / 41 gold
- SOCKS4: 222 alive / 123 gold
- SOCKS5: 254 alive / 137 gold

## Historical pool

- Discovered: 117088
- Ever alive: 17128
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
