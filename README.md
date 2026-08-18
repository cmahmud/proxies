# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 335
- HTTP: 288 alive / 52 gold
- HTTPS: 193 alive / 13 gold
- SOCKS4: 221 alive / 136 gold
- SOCKS5: 216 alive / 134 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14939
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
