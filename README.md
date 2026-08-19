# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 545
- HTTP: 396 alive / 167 gold
- HTTPS: 246 alive / 91 gold
- SOCKS4: 217 alive / 145 gold
- SOCKS5: 213 alive / 142 gold

## Historical pool

- Discovered: 123168
- Ever alive: 18789
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
