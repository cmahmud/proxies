# SyndProxy private pool

## Current pool

- Alive now: 1721
- Gold now: 647
- HTTP: 709 alive / 246 gold
- HTTPS: 553 alive / 115 gold
- SOCKS4: 204 alive / 128 gold
- SOCKS5: 255 alive / 158 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24793
- Ever gold: 1045

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
