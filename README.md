# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 392
- HTTP: 263 alive / 89 gold
- HTTPS: 156 alive / 20 gold
- SOCKS4: 178 alive / 125 gold
- SOCKS5: 225 alive / 158 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29486
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
