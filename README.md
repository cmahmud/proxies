# SyndProxy private pool

## Current pool

- Alive now: 1563
- Gold now: 646
- HTTP: 593 alive / 238 gold
- HTTPS: 488 alive / 122 gold
- SOCKS4: 232 alive / 146 gold
- SOCKS5: 250 alive / 140 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24654
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
