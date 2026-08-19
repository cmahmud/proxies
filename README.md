# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 415
- HTTP: 383 alive / 82 gold
- HTTPS: 247 alive / 14 gold
- SOCKS4: 257 alive / 156 gold
- SOCKS5: 275 alive / 163 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20706
- Ever gold: 874

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
