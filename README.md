# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 433
- HTTP: 301 alive / 96 gold
- HTTPS: 247 alive / 35 gold
- SOCKS4: 182 alive / 131 gold
- SOCKS5: 256 alive / 171 gold

## Historical pool

- Discovered: 161922
- Ever alive: 31161
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
