# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 403
- HTTP: 319 alive / 91 gold
- HTTPS: 199 alive / 27 gold
- SOCKS4: 215 alive / 136 gold
- SOCKS5: 242 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32098
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
