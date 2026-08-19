# SyndProxy private pool

## Current pool

- Alive now: 1082
- Gold now: 536
- HTTP: 392 alive / 155 gold
- HTTPS: 269 alive / 102 gold
- SOCKS4: 213 alive / 136 gold
- SOCKS5: 208 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19839
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
