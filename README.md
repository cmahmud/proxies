# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 329
- HTTP: 272 alive / 49 gold
- HTTPS: 201 alive / 13 gold
- SOCKS4: 214 alive / 135 gold
- SOCKS5: 212 alive / 132 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14937
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
