# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 405
- HTTP: 76 alive / 51 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47103
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
