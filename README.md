# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 438
- HTTP: 116 alive / 81 gold
- HTTPS: 59 alive / 26 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43690
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
