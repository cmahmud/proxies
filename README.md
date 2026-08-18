# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 234
- HTTP: 186 alive / 29 gold
- HTTPS: 96 alive / 8 gold
- SOCKS4: 206 alive / 113 gold
- SOCKS5: 200 alive / 84 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7594
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
