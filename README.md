# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 526
- HTTP: 433 alive / 188 gold
- HTTPS: 324 alive / 69 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 214 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19773
- Ever gold: 786

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
