# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 334
- HTTP: 283 alive / 52 gold
- HTTPS: 192 alive / 13 gold
- SOCKS4: 222 alive / 136 gold
- SOCKS5: 214 alive / 133 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14939
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
