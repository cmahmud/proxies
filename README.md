# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 357
- HTTP: 174 alive / 68 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 190 alive / 132 gold
- SOCKS5: 197 alive / 139 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25764
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
