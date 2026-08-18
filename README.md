# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 274
- HTTP: 189 alive / 28 gold
- HTTPS: 152 alive / 4 gold
- SOCKS4: 232 alive / 135 gold
- SOCKS5: 210 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12412
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
