# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 355
- HTTP: 189 alive / 73 gold
- HTTPS: 131 alive / 22 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 176 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25349
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
