# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 440
- HTTP: 115 alive / 88 gold
- HTTPS: 144 alive / 22 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42186
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
