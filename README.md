# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 230
- HTTP: 302 alive / 33 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 223 alive / 125 gold
- SOCKS5: 144 alive / 64 gold

## Historical pool

- Discovered: 102861
- Ever alive: 13549
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
