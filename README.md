# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 444
- HTTP: 108 alive / 79 gold
- HTTPS: 88 alive / 31 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47011
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
