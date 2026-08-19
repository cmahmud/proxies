# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 515
- HTTP: 335 alive / 149 gold
- HTTPS: 233 alive / 88 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 205 alive / 130 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17631
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
