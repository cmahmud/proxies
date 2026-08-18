# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 253
- HTTP: 203 alive / 33 gold
- HTTPS: 111 alive / 8 gold
- SOCKS4: 218 alive / 132 gold
- SOCKS5: 170 alive / 80 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9682
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
