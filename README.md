# SyndProxy private pool

## Current pool

- Alive now: 1430
- Gold now: 548
- HTTP: 550 alive / 179 gold
- HTTPS: 408 alive / 83 gold
- SOCKS4: 230 alive / 131 gold
- SOCKS5: 242 alive / 155 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22985
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
