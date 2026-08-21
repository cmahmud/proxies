# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 420
- HTTP: 364 alive / 96 gold
- HTTPS: 271 alive / 24 gold
- SOCKS4: 236 alive / 145 gold
- SOCKS5: 272 alive / 155 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28138
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
