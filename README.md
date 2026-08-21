# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 441
- HTTP: 383 alive / 107 gold
- HTTPS: 264 alive / 32 gold
- SOCKS4: 199 alive / 152 gold
- SOCKS5: 249 alive / 150 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28617
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
