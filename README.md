# SyndProxy private pool

## Current pool

- Alive now: 707
- Gold now: 383
- HTTP: 163 alive / 73 gold
- HTTPS: 128 alive / 19 gold
- SOCKS4: 212 alive / 148 gold
- SOCKS5: 204 alive / 143 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26368
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
