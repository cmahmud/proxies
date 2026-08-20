# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 384
- HTTP: 174 alive / 72 gold
- HTTPS: 156 alive / 17 gold
- SOCKS4: 218 alive / 152 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26391
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
