# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 469
- HTTP: 127 alive / 95 gold
- HTTPS: 115 alive / 38 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46371
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
