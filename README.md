# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 447
- HTTP: 112 alive / 82 gold
- HTTPS: 64 alive / 32 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44587
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
