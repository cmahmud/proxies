# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 425
- HTTP: 356 alive / 98 gold
- HTTPS: 269 alive / 26 gold
- SOCKS4: 239 alive / 145 gold
- SOCKS5: 272 alive / 156 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28139
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
