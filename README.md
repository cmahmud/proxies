# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 377
- HTTP: 173 alive / 67 gold
- HTTPS: 136 alive / 23 gold
- SOCKS4: 207 alive / 146 gold
- SOCKS5: 197 alive / 141 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26349
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
