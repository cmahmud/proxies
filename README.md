# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 355
- HTTP: 185 alive / 75 gold
- HTTPS: 138 alive / 22 gold
- SOCKS4: 190 alive / 129 gold
- SOCKS5: 189 alive / 129 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26634
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
