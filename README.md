# SyndProxy private pool

## Current pool

- Alive now: 1294
- Gold now: 548
- HTTP: 477 alive / 179 gold
- HTTPS: 343 alive / 71 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19570
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
