# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 415
- HTTP: 303 alive / 85 gold
- HTTPS: 199 alive / 26 gold
- SOCKS4: 192 alive / 133 gold
- SOCKS5: 247 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31471
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
