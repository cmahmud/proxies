# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 399
- HTTP: 189 alive / 83 gold
- HTTPS: 163 alive / 28 gold
- SOCKS4: 206 alive / 146 gold
- SOCKS5: 203 alive / 142 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31896
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
