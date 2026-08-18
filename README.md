# SyndProxy private pool

## Current pool

- Alive now: 738
- Gold now: 255
- HTTP: 211 alive / 32 gold
- HTTPS: 118 alive / 8 gold
- SOCKS4: 230 alive / 135 gold
- SOCKS5: 179 alive / 80 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9682
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
