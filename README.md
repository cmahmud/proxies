# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 418
- HTTP: 84 alive / 62 gold
- HTTPS: 40 alive / 22 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
