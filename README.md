# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 365
- HTTP: 190 alive / 70 gold
- HTTPS: 143 alive / 13 gold
- SOCKS4: 210 alive / 146 gold
- SOCKS5: 198 alive / 136 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26396
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
