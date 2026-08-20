# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 402
- HTTP: 176 alive / 72 gold
- HTTPS: 154 alive / 16 gold
- SOCKS4: 224 alive / 157 gold
- SOCKS5: 215 alive / 157 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26392
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
