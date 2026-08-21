# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 402
- HTTP: 300 alive / 96 gold
- HTTPS: 221 alive / 34 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 255 alive / 130 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30919
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
