# SyndProxy private pool

## Current pool

- Alive now: 1110
- Gold now: 437
- HTTP: 380 alive / 95 gold
- HTTPS: 261 alive / 35 gold
- SOCKS4: 207 alive / 139 gold
- SOCKS5: 262 alive / 168 gold

## Historical pool

- Discovered: 161412
- Ever alive: 31134
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
