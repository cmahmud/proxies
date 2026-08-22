# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 387
- HTTP: 239 alive / 88 gold
- HTTPS: 170 alive / 29 gold
- SOCKS4: 207 alive / 138 gold
- SOCKS5: 212 alive / 132 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31625
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
