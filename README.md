# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 384
- HTTP: 165 alive / 75 gold
- HTTPS: 123 alive / 20 gold
- SOCKS4: 214 alive / 150 gold
- SOCKS5: 195 alive / 139 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26241
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
