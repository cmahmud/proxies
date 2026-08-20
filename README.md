# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 342
- HTTP: 203 alive / 70 gold
- HTTPS: 146 alive / 16 gold
- SOCKS4: 211 alive / 139 gold
- SOCKS5: 177 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25359
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
