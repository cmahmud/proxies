# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 415
- HTTP: 345 alive / 96 gold
- HTTPS: 221 alive / 29 gold
- SOCKS4: 226 alive / 143 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29719
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
