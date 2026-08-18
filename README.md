# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 331
- HTTP: 288 alive / 52 gold
- HTTPS: 192 alive / 12 gold
- SOCKS4: 227 alive / 135 gold
- SOCKS5: 221 alive / 132 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14969
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
