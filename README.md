# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 435
- HTTP: 133 alive / 80 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34555
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
