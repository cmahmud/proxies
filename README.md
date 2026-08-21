# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 430
- HTTP: 356 alive / 111 gold
- HTTPS: 204 alive / 28 gold
- SOCKS4: 256 alive / 148 gold
- SOCKS5: 260 alive / 143 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30795
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
