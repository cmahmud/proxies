# SyndProxy private pool

## Current pool

- Alive now: 689
- Gold now: 375
- HTTP: 188 alive / 71 gold
- HTTPS: 117 alive / 19 gold
- SOCKS4: 185 alive / 140 gold
- SOCKS5: 199 alive / 145 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25820
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
