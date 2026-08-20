# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 392
- HTTP: 334 alive / 98 gold
- HTTPS: 221 alive / 26 gold
- SOCKS4: 250 alive / 132 gold
- SOCKS5: 268 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25096
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
