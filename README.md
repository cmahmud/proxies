# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 388
- HTTP: 221 alive / 80 gold
- HTTPS: 248 alive / 24 gold
- SOCKS4: 225 alive / 146 gold
- SOCKS5: 202 alive / 138 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31871
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
