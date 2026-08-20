# SyndProxy private pool

## Current pool

- Alive now: 635
- Gold now: 383
- HTTP: 145 alive / 61 gold
- HTTPS: 75 alive / 14 gold
- SOCKS4: 202 alive / 153 gold
- SOCKS5: 213 alive / 155 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25719
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
