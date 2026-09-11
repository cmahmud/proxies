# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 405
- HTTP: 92 alive / 67 gold
- HTTPS: 32 alive / 21 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48794
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
