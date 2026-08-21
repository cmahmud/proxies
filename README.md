# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 389
- HTTP: 297 alive / 76 gold
- HTTPS: 194 alive / 19 gold
- SOCKS4: 195 alive / 131 gold
- SOCKS5: 231 alive / 163 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29685
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
