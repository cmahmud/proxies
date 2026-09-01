# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 405
- HTTP: 70 alive / 50 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47111
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
