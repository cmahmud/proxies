# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 389
- HTTP: 114 alive / 65 gold
- HTTPS: 91 alive / 21 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 198 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39346
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
