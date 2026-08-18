# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 271
- HTTP: 248 alive / 30 gold
- HTTPS: 121 alive / 5 gold
- SOCKS4: 210 alive / 131 gold
- SOCKS5: 207 alive / 105 gold

## Historical pool

- Discovered: 99053
- Ever alive: 11134
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
