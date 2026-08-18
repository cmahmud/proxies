# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 333
- HTTP: 288 alive / 52 gold
- HTTPS: 204 alive / 12 gold
- SOCKS4: 230 alive / 136 gold
- SOCKS5: 217 alive / 133 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14954
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
