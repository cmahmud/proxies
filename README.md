# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 410
- HTTP: 209 alive / 88 gold
- HTTPS: 163 alive / 22 gold
- SOCKS4: 196 alive / 144 gold
- SOCKS5: 210 alive / 156 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27412
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
