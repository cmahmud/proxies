# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 551
- HTTP: 449 alive / 193 gold
- HTTPS: 309 alive / 116 gold
- SOCKS4: 209 alive / 113 gold
- SOCKS5: 197 alive / 129 gold

## Historical pool

- Discovered: 124849
- Ever alive: 19397
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
