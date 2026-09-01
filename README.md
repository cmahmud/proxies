# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 449
- HTTP: 100 alive / 77 gold
- HTTPS: 114 alive / 32 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47425
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
