# SyndProxy private pool

## Current pool

- Alive now: 1298
- Gold now: 520
- HTTP: 494 alive / 185 gold
- HTTPS: 354 alive / 51 gold
- SOCKS4: 201 alive / 124 gold
- SOCKS5: 249 alive / 160 gold

## Historical pool

- Discovered: 125669
- Ever alive: 19647
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
