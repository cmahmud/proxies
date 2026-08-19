# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 562
- HTTP: 430 alive / 186 gold
- HTTPS: 315 alive / 72 gold
- SOCKS4: 245 alive / 153 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19772
- Ever gold: 786

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
