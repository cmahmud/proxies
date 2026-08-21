# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 368
- HTTP: 297 alive / 84 gold
- HTTPS: 192 alive / 21 gold
- SOCKS4: 209 alive / 127 gold
- SOCKS5: 223 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29820
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
