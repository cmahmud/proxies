# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 360
- HTTP: 240 alive / 81 gold
- HTTPS: 184 alive / 27 gold
- SOCKS4: 192 alive / 119 gold
- SOCKS5: 211 alive / 133 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29775
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
