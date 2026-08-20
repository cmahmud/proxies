# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 410
- HTTP: 384 alive / 98 gold
- HTTPS: 255 alive / 21 gold
- SOCKS4: 197 alive / 128 gold
- SOCKS5: 320 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24863
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
