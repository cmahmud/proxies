# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 251
- HTTP: 208 alive / 31 gold
- HTTPS: 112 alive / 8 gold
- SOCKS4: 216 alive / 131 gold
- SOCKS5: 172 alive / 81 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9682
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
