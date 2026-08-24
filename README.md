# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 385
- HTTP: 120 alive / 63 gold
- HTTPS: 44 alive / 15 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 176375
- Ever alive: 33205
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
