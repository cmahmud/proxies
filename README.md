# SyndProxy private pool

## Current pool

- Alive now: 1050
- Gold now: 384
- HTTP: 335 alive / 94 gold
- HTTPS: 223 alive / 22 gold
- SOCKS4: 234 alive / 132 gold
- SOCKS5: 258 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25075
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
