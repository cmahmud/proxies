# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 417
- HTTP: 116 alive / 79 gold
- HTTPS: 115 alive / 16 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42090
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
