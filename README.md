# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 334
- HTTP: 326 alive / 85 gold
- HTTPS: 216 alive / 20 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 202 alive / 88 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32489
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
