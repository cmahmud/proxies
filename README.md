# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 476
- HTTP: 161 alive / 100 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 218 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45253
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
