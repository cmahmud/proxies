# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 397
- HTTP: 191 alive / 72 gold
- HTTPS: 149 alive / 17 gold
- SOCKS4: 221 alive / 159 gold
- SOCKS5: 219 alive / 149 gold

## Historical pool

- Discovered: 147653
- Ever alive: 25888
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
