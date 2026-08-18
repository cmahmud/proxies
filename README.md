# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 335
- HTTP: 275 alive / 52 gold
- HTTPS: 195 alive / 13 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 218 alive / 134 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14937
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
