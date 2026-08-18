# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 362
- HTTP: 335 alive / 54 gold
- HTTPS: 221 alive / 13 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 241 alive / 151 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14870
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
