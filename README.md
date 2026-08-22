# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 416
- HTTP: 223 alive / 85 gold
- HTTPS: 182 alive / 27 gold
- SOCKS4: 185 alive / 133 gold
- SOCKS5: 246 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31469
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
