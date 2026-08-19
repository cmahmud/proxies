# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 588
- HTTP: 390 alive / 172 gold
- HTTPS: 315 alive / 145 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 190 alive / 128 gold

## Historical pool

- Discovered: 127408
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
