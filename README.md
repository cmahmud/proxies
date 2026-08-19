# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 529
- HTTP: 380 alive / 159 gold
- HTTPS: 280 alive / 92 gold
- SOCKS4: 220 alive / 140 gold
- SOCKS5: 229 alive / 138 gold

## Historical pool

- Discovered: 122361
- Ever alive: 18541
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
