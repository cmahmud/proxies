# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 328
- HTTP: 122 alive / 37 gold
- HTTPS: 47 alive / 8 gold
- SOCKS4: 164 alive / 141 gold
- SOCKS5: 176 alive / 142 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32786
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
