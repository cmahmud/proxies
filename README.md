# SyndProxy private pool

## Current pool

- Alive now: 624
- Gold now: 225
- HTTP: 195 alive / 37 gold
- HTTPS: 91 alive / 10 gold
- SOCKS4: 162 alive / 101 gold
- SOCKS5: 176 alive / 77 gold

## Historical pool

- Discovered: 86650
- Ever alive: 5726
- Ever gold: 293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
