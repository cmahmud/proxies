# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 189
- HTTP: 179 alive / 38 gold
- HTTPS: 76 alive / 6 gold
- SOCKS4: 90 alive / 65 gold
- SOCKS5: 136 alive / 80 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32751
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
