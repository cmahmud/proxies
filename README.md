# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 374
- HTTP: 246 alive / 63 gold
- HTTPS: 95 alive / 17 gold
- SOCKS4: 186 alive / 149 gold
- SOCKS5: 210 alive / 145 gold

## Historical pool

- Discovered: 146664
- Ever alive: 25745
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
