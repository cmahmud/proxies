# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 366
- HTTP: 307 alive / 71 gold
- HTTPS: 181 alive / 21 gold
- SOCKS4: 189 alive / 128 gold
- SOCKS5: 209 alive / 146 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29670
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
