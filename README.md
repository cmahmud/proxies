# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 364
- HTTP: 194 alive / 70 gold
- HTTPS: 151 alive / 13 gold
- SOCKS4: 205 alive / 146 gold
- SOCKS5: 192 alive / 135 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26396
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
