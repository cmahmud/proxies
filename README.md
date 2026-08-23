# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 340
- HTTP: 114 alive / 38 gold
- HTTPS: 51 alive / 7 gold
- SOCKS4: 178 alive / 154 gold
- SOCKS5: 189 alive / 141 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32890
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
