# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 398
- HTTP: 333 alive / 78 gold
- HTTPS: 229 alive / 16 gold
- SOCKS4: 265 alive / 148 gold
- SOCKS5: 235 alive / 156 gold

## Historical pool

- Discovered: 131098
- Ever alive: 20518
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
