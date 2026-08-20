# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 594
- HTTP: 417 alive / 188 gold
- HTTPS: 312 alive / 96 gold
- SOCKS4: 231 alive / 146 gold
- SOCKS5: 247 alive / 164 gold

## Historical pool

- Discovered: 139662
- Ever alive: 23523
- Ever gold: 922

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
