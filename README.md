# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 407
- HTTP: 90 alive / 62 gold
- HTTPS: 44 alive / 17 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48865
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
