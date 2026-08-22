# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 394
- HTTP: 311 alive / 87 gold
- HTTPS: 234 alive / 25 gold
- SOCKS4: 220 alive / 124 gold
- SOCKS5: 259 alive / 158 gold

## Historical pool

- Discovered: 164912
- Ever alive: 32132
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
