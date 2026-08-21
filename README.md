# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 386
- HTTP: 235 alive / 81 gold
- HTTPS: 102 alive / 16 gold
- SOCKS4: 196 alive / 137 gold
- SOCKS5: 241 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29756
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
