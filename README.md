# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 445
- HTTP: 293 alive / 85 gold
- HTTPS: 205 alive / 32 gold
- SOCKS4: 225 alive / 155 gold
- SOCKS5: 239 alive / 173 gold

## Historical pool

- Discovered: 163874
- Ever alive: 32020
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
