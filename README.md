# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 378
- HTTP: 238 alive / 84 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 205 alive / 115 gold
- SOCKS5: 245 alive / 156 gold

## Historical pool

- Discovered: 166449
- Ever alive: 32401
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
