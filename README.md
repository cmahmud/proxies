# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 409
- HTTP: 443 alive / 91 gold
- HTTPS: 226 alive / 29 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 233 alive / 156 gold

## Historical pool

- Discovered: 163042
- Ever alive: 31683
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
