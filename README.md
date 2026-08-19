# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 528
- HTTP: 371 alive / 160 gold
- HTTPS: 272 alive / 91 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 229 alive / 138 gold

## Historical pool

- Discovered: 122361
- Ever alive: 18549
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
