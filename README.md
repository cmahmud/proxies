# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 332
- HTTP: 283 alive / 53 gold
- HTTPS: 191 alive / 13 gold
- SOCKS4: 222 alive / 132 gold
- SOCKS5: 223 alive / 134 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14969
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
