# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 405
- HTTP: 220 alive / 91 gold
- HTTPS: 143 alive / 26 gold
- SOCKS4: 214 alive / 136 gold
- SOCKS5: 244 alive / 152 gold

## Historical pool

- Discovered: 154731
- Ever alive: 29172
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
