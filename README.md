# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 396
- HTTP: 209 alive / 81 gold
- HTTPS: 180 alive / 26 gold
- SOCKS4: 213 alive / 145 gold
- SOCKS5: 205 alive / 144 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31893
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
