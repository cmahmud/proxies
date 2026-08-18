# SyndProxy private pool

## Current pool

- Alive now: 634
- Gold now: 223
- HTTP: 179 alive / 32 gold
- HTTPS: 77 alive / 8 gold
- SOCKS4: 191 alive / 106 gold
- SOCKS5: 187 alive / 77 gold

## Historical pool

- Discovered: 86707
- Ever alive: 6452
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
