# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 363
- HTTP: 323 alive / 82 gold
- HTTPS: 200 alive / 18 gold
- SOCKS4: 208 alive / 121 gold
- SOCKS5: 216 alive / 142 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29808
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
