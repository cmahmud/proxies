# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 411
- HTTP: 85 alive / 63 gold
- HTTPS: 36 alive / 19 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48859
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
