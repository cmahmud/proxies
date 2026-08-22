# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 399
- HTTP: 204 alive / 82 gold
- HTTPS: 163 alive / 27 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31896
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
