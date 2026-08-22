# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 415
- HTTP: 218 alive / 90 gold
- HTTPS: 167 alive / 24 gold
- SOCKS4: 206 alive / 144 gold
- SOCKS5: 237 alive / 157 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31849
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
