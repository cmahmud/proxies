# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 410
- HTTP: 84 alive / 63 gold
- HTTPS: 40 alive / 21 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48833
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
