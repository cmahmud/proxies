# SyndProxy private pool

## Current pool

- Alive now: 1259
- Gold now: 514
- HTTP: 455 alive / 181 gold
- HTTPS: 360 alive / 51 gold
- SOCKS4: 205 alive / 122 gold
- SOCKS5: 239 alive / 160 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19634
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
