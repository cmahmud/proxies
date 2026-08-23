# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 196
- HTTP: 273 alive / 35 gold
- HTTPS: 47 alive / 5 gold
- SOCKS4: 184 alive / 68 gold
- SOCKS5: 195 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32775
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
