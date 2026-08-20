# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 373
- HTTP: 179 alive / 68 gold
- HTTPS: 101 alive / 19 gold
- SOCKS4: 190 alive / 140 gold
- SOCKS5: 194 alive / 146 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25820
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
