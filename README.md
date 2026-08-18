# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 355
- HTTP: 291 alive / 51 gold
- HTTPS: 194 alive / 16 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 237 alive / 141 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14791
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
