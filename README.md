# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 386
- HTTP: 201 alive / 65 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 201 alive / 151 gold
- SOCKS5: 213 alive / 152 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25730
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
