# SyndProxy private pool

## Current pool

- Alive now: 1835
- Gold now: 654
- HTTP: 709 alive / 211 gold
- HTTPS: 533 alive / 114 gold
- SOCKS4: 247 alive / 159 gold
- SOCKS5: 346 alive / 170 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24182
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
