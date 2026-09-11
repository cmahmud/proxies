# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 423
- HTTP: 99 alive / 70 gold
- HTTPS: 50 alive / 24 gold
- SOCKS4: 188 alive / 166 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49035
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
