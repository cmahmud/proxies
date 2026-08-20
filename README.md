# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 390
- HTTP: 319 alive / 77 gold
- HTTPS: 189 alive / 22 gold
- SOCKS4: 190 alive / 127 gold
- SOCKS5: 233 alive / 164 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27137
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
