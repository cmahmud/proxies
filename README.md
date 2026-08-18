# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 257
- HTTP: 202 alive / 34 gold
- HTTPS: 107 alive / 8 gold
- SOCKS4: 221 alive / 135 gold
- SOCKS5: 172 alive / 80 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9682
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
