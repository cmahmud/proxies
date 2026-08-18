# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 252
- HTTP: 190 alive / 32 gold
- HTTPS: 109 alive / 8 gold
- SOCKS4: 214 alive / 131 gold
- SOCKS5: 173 alive / 81 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9683
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
