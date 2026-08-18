# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 327
- HTTP: 253 alive / 48 gold
- HTTPS: 200 alive / 13 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 208 alive / 132 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14937
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
