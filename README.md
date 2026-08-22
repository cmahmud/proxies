# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 409
- HTTP: 355 alive / 92 gold
- HTTPS: 216 alive / 23 gold
- SOCKS4: 226 alive / 135 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32432
- Ever gold: 1181

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
