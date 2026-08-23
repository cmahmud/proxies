# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 375
- HTTP: 105 alive / 62 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 162 alive / 145 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 174154
- Ever alive: 33073
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
