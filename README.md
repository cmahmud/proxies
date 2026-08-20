# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 391
- HTTP: 180 alive / 66 gold
- HTTPS: 82 alive / 14 gold
- SOCKS4: 200 alive / 153 gold
- SOCKS5: 207 alive / 158 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25721
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
