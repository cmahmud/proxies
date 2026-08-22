# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 395
- HTTP: 213 alive / 80 gold
- HTTPS: 185 alive / 26 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 214 alive / 145 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31892
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
