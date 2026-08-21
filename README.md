# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 410
- HTTP: 350 alive / 102 gold
- HTTPS: 247 alive / 25 gold
- SOCKS4: 245 alive / 155 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30832
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
