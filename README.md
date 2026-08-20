# SyndProxy private pool

## Current pool

- Alive now: 1609
- Gold now: 613
- HTTP: 605 alive / 234 gold
- HTTPS: 508 alive / 117 gold
- SOCKS4: 196 alive / 99 gold
- SOCKS5: 300 alive / 163 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24660
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
