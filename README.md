# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 297
- HTTP: 142 alive / 72 gold
- HTTPS: 34 alive / 18 gold
- SOCKS4: 116 alive / 68 gold
- SOCKS5: 181 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1477

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
