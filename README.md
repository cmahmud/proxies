# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 421
- HTTP: 391 alive / 90 gold
- HTTPS: 231 alive / 29 gold
- SOCKS4: 258 alive / 147 gold
- SOCKS5: 273 alive / 155 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32166
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
