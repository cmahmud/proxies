# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 400
- HTTP: 160 alive / 72 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 202 alive / 155 gold
- SOCKS5: 212 alive / 150 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26759
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
