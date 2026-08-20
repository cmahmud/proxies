# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 373
- HTTP: 164 alive / 66 gold
- HTTPS: 135 alive / 21 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 204 alive / 140 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26333
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
