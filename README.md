# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 377
- HTTP: 78 alive / 51 gold
- HTTPS: 35 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48320
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
