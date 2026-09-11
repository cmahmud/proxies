# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 409
- HTTP: 87 alive / 63 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48864
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
