# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 526
- HTTP: 375 alive / 159 gold
- HTTPS: 267 alive / 92 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 226 alive / 135 gold

## Historical pool

- Discovered: 122361
- Ever alive: 18539
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
