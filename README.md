# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 419
- HTTP: 115 alive / 78 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42080
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
