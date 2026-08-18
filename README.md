# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 242
- HTTP: 396 alive / 32 gold
- HTTPS: 139 alive / 6 gold
- SOCKS4: 227 alive / 139 gold
- SOCKS5: 153 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13646
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
