# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 428
- HTTP: 107 alive / 76 gold
- HTTPS: 43 alive / 18 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48980
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
