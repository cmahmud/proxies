# SyndProxy private pool

## Current pool

- Alive now: 632
- Gold now: 223
- HTTP: 195 alive / 35 gold
- HTTPS: 92 alive / 10 gold
- SOCKS4: 162 alive / 103 gold
- SOCKS5: 183 alive / 75 gold

## Historical pool

- Discovered: 86650
- Ever alive: 5726
- Ever gold: 293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
