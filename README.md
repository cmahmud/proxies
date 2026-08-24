# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 426
- HTTP: 138 alive / 74 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33909
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
