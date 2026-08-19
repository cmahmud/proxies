# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 530
- HTTP: 370 alive / 160 gold
- HTTPS: 264 alive / 92 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 227 alive / 138 gold

## Historical pool

- Discovered: 122361
- Ever alive: 18549
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
