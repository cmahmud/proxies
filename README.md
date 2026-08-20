# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 372
- HTTP: 155 alive / 65 gold
- HTTPS: 152 alive / 17 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 198 alive / 141 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26386
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
