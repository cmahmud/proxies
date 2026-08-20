# SyndProxy private pool

## Current pool

- Alive now: 697
- Gold now: 354
- HTTP: 178 alive / 74 gold
- HTTPS: 137 alive / 18 gold
- SOCKS4: 215 alive / 144 gold
- SOCKS5: 167 alive / 118 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25353
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
