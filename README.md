# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 391
- HTTP: 79 alive / 52 gold
- HTTPS: 57 alive / 20 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42793
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
