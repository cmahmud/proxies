# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 414
- HTTP: 84 alive / 63 gold
- HTTPS: 37 alive / 22 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48824
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
