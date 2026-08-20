# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 375
- HTTP: 160 alive / 67 gold
- HTTPS: 142 alive / 22 gold
- SOCKS4: 209 alive / 146 gold
- SOCKS5: 197 alive / 140 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26345
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
