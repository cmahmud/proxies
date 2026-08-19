# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 520
- HTTP: 372 alive / 161 gold
- HTTPS: 271 alive / 88 gold
- SOCKS4: 222 alive / 139 gold
- SOCKS5: 218 alive / 132 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18514
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
