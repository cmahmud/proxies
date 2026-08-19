# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 548
- HTTP: 421 alive / 190 gold
- HTTPS: 301 alive / 80 gold
- SOCKS4: 223 alive / 133 gold
- SOCKS5: 207 alive / 145 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19825
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
