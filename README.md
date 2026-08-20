# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 375
- HTTP: 192 alive / 68 gold
- HTTPS: 133 alive / 22 gold
- SOCKS4: 206 alive / 146 gold
- SOCKS5: 193 alive / 139 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26354
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
