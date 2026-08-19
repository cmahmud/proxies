# SyndProxy private pool

## Current pool

- Alive now: 1288
- Gold now: 532
- HTTP: 496 alive / 185 gold
- HTTPS: 353 alive / 59 gold
- SOCKS4: 201 alive / 124 gold
- SOCKS5: 238 alive / 164 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19663
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
