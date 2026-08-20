# SyndProxy private pool

## Current pool

- Alive now: 670
- Gold now: 375
- HTTP: 185 alive / 69 gold
- HTTPS: 96 alive / 19 gold
- SOCKS4: 191 alive / 141 gold
- SOCKS5: 198 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25823
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
