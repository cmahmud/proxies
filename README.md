# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 381
- HTTP: 155 alive / 58 gold
- HTTPS: 104 alive / 20 gold
- SOCKS4: 206 alive / 152 gold
- SOCKS5: 203 alive / 151 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25728
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
