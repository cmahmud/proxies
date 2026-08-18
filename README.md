# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 225
- HTTP: 281 alive / 27 gold
- HTTPS: 153 alive / 7 gold
- SOCKS4: 240 alive / 110 gold
- SOCKS5: 216 alive / 81 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
