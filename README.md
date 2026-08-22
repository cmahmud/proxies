# SyndProxy private pool

## Current pool

- Alive now: 735
- Gold now: 410
- HTTP: 187 alive / 85 gold
- HTTPS: 133 alive / 27 gold
- SOCKS4: 192 alive / 139 gold
- SOCKS5: 223 alive / 159 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31421
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
