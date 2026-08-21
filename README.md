# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 398
- HTTP: 248 alive / 85 gold
- HTTPS: 154 alive / 19 gold
- SOCKS4: 219 alive / 146 gold
- SOCKS5: 222 alive / 148 gold

## Historical pool

- Discovered: 155802
- Ever alive: 29403
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
