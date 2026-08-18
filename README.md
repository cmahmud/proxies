# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 254
- HTTP: 226 alive / 30 gold
- HTTPS: 147 alive / 8 gold
- SOCKS4: 222 alive / 136 gold
- SOCKS5: 186 alive / 80 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9679
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
