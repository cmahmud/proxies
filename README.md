# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 378
- HTTP: 157 alive / 66 gold
- HTTPS: 158 alive / 19 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 202 alive / 144 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26385
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
