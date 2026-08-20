# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 385
- HTTP: 167 alive / 63 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 207 alive / 151 gold
- SOCKS5: 201 alive / 152 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25728
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
