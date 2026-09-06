# SyndProxy validated proxy pool

## Current pool

- Alive now: 436
- Gold now: 319
- HTTP: 85 alive / 59 gold
- HTTPS: 32 alive / 6 gold
- SOCKS4: 146 alive / 137 gold
- SOCKS5: 173 alive / 117 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48400
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
