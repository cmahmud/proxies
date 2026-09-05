# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 299
- HTTP: 164 alive / 73 gold
- HTTPS: 40 alive / 23 gold
- SOCKS4: 216 alive / 68 gold
- SOCKS5: 204 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47802
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
