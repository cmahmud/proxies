# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 417
- HTTP: 277 alive / 94 gold
- HTTPS: 236 alive / 26 gold
- SOCKS4: 242 alive / 150 gold
- SOCKS5: 254 alive / 147 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25205
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
