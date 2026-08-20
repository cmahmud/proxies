# SyndProxy private pool

## Current pool

- Alive now: 1766
- Gold now: 701
- HTTP: 660 alive / 233 gold
- HTTPS: 545 alive / 144 gold
- SOCKS4: 232 alive / 158 gold
- SOCKS5: 329 alive / 166 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24376
- Ever gold: 1021

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
