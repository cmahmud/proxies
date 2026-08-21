# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 403
- HTTP: 223 alive / 90 gold
- HTTPS: 163 alive / 25 gold
- SOCKS4: 192 alive / 128 gold
- SOCKS5: 215 alive / 160 gold

## Historical pool

- Discovered: 151684
- Ever alive: 27704
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
