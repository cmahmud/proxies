# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 424
- HTTP: 90 alive / 65 gold
- HTTPS: 44 alive / 25 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
