# SyndProxy private pool

## Current pool

- Alive now: 796
- Gold now: 386
- HTTP: 205 alive / 74 gold
- HTTPS: 167 alive / 24 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 215 alive / 144 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31892
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
