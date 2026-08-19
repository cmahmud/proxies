# SyndProxy private pool

## Current pool

- Alive now: 1301
- Gold now: 512
- HTTP: 482 alive / 182 gold
- HTTPS: 369 alive / 48 gold
- SOCKS4: 206 alive / 122 gold
- SOCKS5: 244 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
