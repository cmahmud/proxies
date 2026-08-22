# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 415
- HTTP: 257 alive / 86 gold
- HTTPS: 179 alive / 32 gold
- SOCKS4: 198 alive / 146 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31850
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
