# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 403
- HTTP: 392 alive / 93 gold
- HTTPS: 270 alive / 14 gold
- SOCKS4: 235 alive / 147 gold
- SOCKS5: 247 alive / 149 gold

## Historical pool

- Discovered: 131843
- Ever alive: 21233
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
