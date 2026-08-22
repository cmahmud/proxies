# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 445
- HTTP: 294 alive / 85 gold
- HTTPS: 204 alive / 31 gold
- SOCKS4: 223 alive / 157 gold
- SOCKS5: 237 alive / 172 gold

## Historical pool

- Discovered: 163874
- Ever alive: 32022
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
