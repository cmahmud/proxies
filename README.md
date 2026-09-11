# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 407
- HTTP: 84 alive / 62 gold
- HTTPS: 46 alive / 21 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 175 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48839
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
