# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 286
- HTTP: 120 alive / 63 gold
- HTTPS: 193 alive / 35 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48479
- Ever gold: 1540

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
