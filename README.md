# SyndProxy private pool

## Current pool

- Alive now: 613
- Gold now: 233
- HTTP: 194 alive / 30 gold
- HTTPS: 73 alive / 8 gold
- SOCKS4: 182 alive / 110 gold
- SOCKS5: 164 alive / 85 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6457
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
