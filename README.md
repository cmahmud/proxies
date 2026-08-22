# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 435
- HTTP: 256 alive / 89 gold
- HTTPS: 173 alive / 33 gold
- SOCKS4: 200 alive / 148 gold
- SOCKS5: 239 alive / 165 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31522
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
