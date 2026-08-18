# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 214
- HTTP: 242 alive / 26 gold
- HTTPS: 140 alive / 9 gold
- SOCKS4: 191 alive / 96 gold
- SOCKS5: 225 alive / 83 gold

## Historical pool

- Discovered: 91700
- Ever alive: 8643
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
