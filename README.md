# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 522
- HTTP: 391 alive / 151 gold
- HTTPS: 247 alive / 83 gold
- SOCKS4: 236 alive / 152 gold
- SOCKS5: 204 alive / 136 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17987
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
