# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 592
- HTTP: 382 alive / 189 gold
- HTTPS: 340 alive / 102 gold
- SOCKS4: 211 alive / 146 gold
- SOCKS5: 235 alive / 155 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23451
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
