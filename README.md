# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 391
- HTTP: 191 alive / 76 gold
- HTTPS: 164 alive / 18 gold
- SOCKS4: 194 alive / 148 gold
- SOCKS5: 215 alive / 149 gold

## Historical pool

- Discovered: 148345
- Ever alive: 26434
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
