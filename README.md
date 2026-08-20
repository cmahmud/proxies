# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 388
- HTTP: 198 alive / 64 gold
- HTTPS: 86 alive / 14 gold
- SOCKS4: 210 alive / 153 gold
- SOCKS5: 211 alive / 157 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25721
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
