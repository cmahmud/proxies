# SyndProxy private pool

## Current pool

- Alive now: 1102
- Gold now: 355
- HTTP: 402 alive / 53 gold
- HTTPS: 238 alive / 13 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 236 alive / 148 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14868
- Ever gold: 477

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
