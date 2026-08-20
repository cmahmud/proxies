# SyndProxy private pool

## Current pool

- Alive now: 706
- Gold now: 385
- HTTP: 168 alive / 75 gold
- HTTPS: 131 alive / 20 gold
- SOCKS4: 204 alive / 147 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26366
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
