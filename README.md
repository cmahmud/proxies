# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 347
- HTTP: 297 alive / 51 gold
- HTTPS: 183 alive / 14 gold
- SOCKS4: 212 alive / 133 gold
- SOCKS5: 217 alive / 149 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14915
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
