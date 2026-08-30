# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 447
- HTTP: 119 alive / 83 gold
- HTTPS: 74 alive / 32 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44591
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
