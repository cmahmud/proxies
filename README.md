# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 428
- HTTP: 313 alive / 84 gold
- HTTPS: 229 alive / 27 gold
- SOCKS4: 232 alive / 155 gold
- SOCKS5: 263 alive / 162 gold

## Historical pool

- Discovered: 163866
- Ever alive: 31994
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
