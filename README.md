# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 342
- HTTP: 116 alive / 40 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 176 alive / 153 gold
- SOCKS5: 190 alive / 141 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32890
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
