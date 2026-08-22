# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 403
- HTTP: 283 alive / 89 gold
- HTTPS: 208 alive / 28 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 243 alive / 136 gold

## Historical pool

- Discovered: 161993
- Ever alive: 31325
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
