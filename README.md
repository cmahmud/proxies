# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 452
- HTTP: 358 alive / 107 gold
- HTTPS: 234 alive / 36 gold
- SOCKS4: 191 alive / 148 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 153732
- Ever alive: 28668
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
