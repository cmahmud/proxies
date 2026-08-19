# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 360
- HTTP: 258 alive / 84 gold
- HTTPS: 150 alive / 16 gold
- SOCKS4: 210 alive / 140 gold
- SOCKS5: 193 alive / 120 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18316
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
