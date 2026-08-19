# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 559
- HTTP: 416 alive / 188 gold
- HTTPS: 283 alive / 111 gold
- SOCKS4: 200 alive / 121 gold
- SOCKS5: 202 alive / 139 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19301
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
