# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 420
- HTTP: 290 alive / 85 gold
- HTTPS: 205 alive / 25 gold
- SOCKS4: 245 alive / 150 gold
- SOCKS5: 258 alive / 160 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32007
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
