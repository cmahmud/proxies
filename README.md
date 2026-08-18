# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 254
- HTTP: 203 alive / 27 gold
- HTTPS: 128 alive / 9 gold
- SOCKS4: 193 alive / 117 gold
- SOCKS5: 220 alive / 101 gold

## Historical pool

- Discovered: 95227
- Ever alive: 10177
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
