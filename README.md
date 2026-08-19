# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 559
- HTTP: 420 alive / 189 gold
- HTTPS: 281 alive / 111 gold
- SOCKS4: 191 alive / 120 gold
- SOCKS5: 204 alive / 139 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19303
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
