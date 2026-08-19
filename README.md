# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 473
- HTTP: 304 alive / 136 gold
- HTTPS: 247 alive / 90 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 193 alive / 110 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17341
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
