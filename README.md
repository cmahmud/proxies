# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 419
- HTTP: 256 alive / 92 gold
- HTTPS: 193 alive / 26 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 237 alive / 157 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31839
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
