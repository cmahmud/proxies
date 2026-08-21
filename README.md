# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 416
- HTTP: 250 alive / 84 gold
- HTTPS: 179 alive / 27 gold
- SOCKS4: 205 alive / 150 gold
- SOCKS5: 240 alive / 155 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28931
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
