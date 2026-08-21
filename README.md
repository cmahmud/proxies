# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 409
- HTTP: 238 alive / 92 gold
- HTTPS: 135 alive / 18 gold
- SOCKS4: 194 alive / 147 gold
- SOCKS5: 223 alive / 152 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27845
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
