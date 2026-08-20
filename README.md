# SyndProxy private pool

## Current pool

- Alive now: 687
- Gold now: 377
- HTTP: 192 alive / 71 gold
- HTTPS: 100 alive / 20 gold
- SOCKS4: 198 alive / 141 gold
- SOCKS5: 197 alive / 145 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25820
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
