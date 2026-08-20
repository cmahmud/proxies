# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 386
- HTTP: 188 alive / 72 gold
- HTTPS: 153 alive / 14 gold
- SOCKS4: 212 alive / 152 gold
- SOCKS5: 203 alive / 148 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26393
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
