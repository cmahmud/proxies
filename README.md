# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 253
- HTTP: 170 alive / 30 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 203 alive / 131 gold
- SOCKS5: 173 alive / 84 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9683
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
