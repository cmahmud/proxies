# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 385
- HTTP: 260 alive / 71 gold
- HTTPS: 172 alive / 21 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 227 alive / 151 gold

## Historical pool

- Discovered: 157410
- Ever alive: 29681
- Ever gold: 1136

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
