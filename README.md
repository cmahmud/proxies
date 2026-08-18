# SyndProxy private pool

## Current pool

- Alive now: 496
- Gold now: 167
- HTTP: 137 alive / 36 gold
- HTTPS: 80 alive / 11 gold
- SOCKS4: 138 alive / 76 gold
- SOCKS5: 141 alive / 44 gold

## Historical pool

- Discovered: 82962
- Ever alive: 5060
- Ever gold: 282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
