# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 380
- HTTP: 125 alive / 60 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 174348
- Ever alive: 33085
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
