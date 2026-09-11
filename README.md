# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 407
- HTTP: 88 alive / 63 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48850
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
