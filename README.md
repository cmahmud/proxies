# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 404
- HTTP: 87 alive / 62 gold
- HTTPS: 40 alive / 20 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48820
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
