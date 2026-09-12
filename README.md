# SyndProxy validated proxy pool

## Current pool

- Alive now: 404
- Gold now: 339
- HTTP: 88 alive / 65 gold
- HTTPS: 32 alive / 17 gold
- SOCKS4: 131 alive / 118 gold
- SOCKS5: 153 alive / 139 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49550
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
