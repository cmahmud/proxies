# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 378
- HTTP: 165 alive / 68 gold
- HTTPS: 143 alive / 19 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 205 alive / 143 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26374
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
