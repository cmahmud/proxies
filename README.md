# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 242
- HTTP: 407 alive / 32 gold
- HTTPS: 148 alive / 6 gold
- SOCKS4: 228 alive / 139 gold
- SOCKS5: 154 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13645
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
