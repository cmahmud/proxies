# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 353
- HTTP: 233 alive / 65 gold
- HTTPS: 120 alive / 17 gold
- SOCKS4: 191 alive / 132 gold
- SOCKS5: 189 alive / 139 gold

## Historical pool

- Discovered: 147168
- Ever alive: 25774
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
