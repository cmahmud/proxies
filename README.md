# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 412
- HTTP: 224 alive / 95 gold
- HTTPS: 153 alive / 27 gold
- SOCKS4: 178 alive / 129 gold
- SOCKS5: 220 alive / 161 gold

## Historical pool

- Discovered: 162701
- Ever alive: 31454
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
