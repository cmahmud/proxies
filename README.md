# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 418
- HTTP: 95 alive / 66 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35616
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
