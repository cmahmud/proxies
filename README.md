# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 442
- HTTP: 137 alive / 86 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34384
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
