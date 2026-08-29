# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 444
- HTTP: 123 alive / 86 gold
- HTTPS: 52 alive / 29 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43667
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
